#![allow(dead_code)]

pub fn str_to_opt_i32(line: &str) -> Option<i32> {
    line.parse::<i32>().ok()
}

/// Quick conversion function from str to i32
pub fn str_to_i32(line: &str) -> i32 {
    line.parse::<i32>().expect(line)
}

pub fn str_to_char_vec(line: &str) -> Vec<char> {
    line.chars().collect()
}

pub fn identity<R>(input: R) -> R {
    input
}

pub fn comma_separated_str_to_vec<R>(line: &str, sub: fn(&str) -> R) -> Vec<R> {
    let parts = line.split(',');
    parts.map(sub).collect()
}