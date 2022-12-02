#![feature(result_option_inspect)]


use parsers::{str_to_opt_i32};
use wrapper::run_day_raw_lines;

use crate::days::day1::{day1_a, day1_b};
use crate::days::day2::{day2_a, day2_b};
use crate::wrapper::run_day_preprocess_lines;

mod wrapper;
mod parsers;

mod days {
    pub(crate) mod day1;
    pub(crate) mod day2;
}

fn main() {
    run_day_preprocess_lines("Day 1 A", "res/day1.txt", str_to_opt_i32, day1_a, Option::Some(70613));
    run_day_preprocess_lines("Day 1 B", "res/day1.txt", str_to_opt_i32, day1_b, Option::Some(205805));
    run_day_raw_lines("Day 2 A", "res/day2.txt", day2_a, Some(14297));
    run_day_raw_lines("Day 2 B", "res/day2.txt", day2_b, Some(10498));
}