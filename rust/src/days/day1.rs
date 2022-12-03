/// 
/// Takes a slice of optional i32s and a mutable results reference to store things
/// within. 
/// 
/// Loops the list, looking for Option::None and creating buckets based on each time
/// it finds a none, then returns the created buckets.
/// 
/// [Some(1), Some(2), None, Some(4), None, Some(6)] => [3, 4, 6]
///
fn sum_slice_split_on_nones(input: &[Option<i32>], results: &mut Vec<i32>) {
    // Ensure we have a starting bucket
    if results.is_empty() {
        results.push(0);
    }
    input.iter().for_each(|next| {
        if let Some(result) = next {
            // Add the result to the last bucket
            *(results.last_mut().unwrap()) += result;
        }
        else {
            // Start a new bucket
            results.push(0);
        }
    });
}

/// Sums the largest `count` items from the given slice.
fn sum_max_n_items(init: &[i32], count: usize) -> i32 {
    let mut sums = vec![0; init.len()];
    sums.clone_from_slice(init);

    // Do the fast sort
    sums.sort_unstable();

    // Reverse the iterator (largest first), take n, sum them
    sums.iter()
        .rev()
        .take(count)
        .sum()
}

pub(crate) fn day1_a(input: &[Option<i32>]) -> i32 {
    let mut results: Vec<i32> = vec![0];
    sum_slice_split_on_nones(input, &mut results);
    sum_max_n_items(results.as_mut_slice(), 1)
}

pub(crate) fn day1_b(input: &[Option<i32>]) -> i32 {
    let mut results: Vec<i32> = vec![0];
    sum_slice_split_on_nones(input, &mut results);
    sum_max_n_items(results.as_mut_slice(), 3)
}