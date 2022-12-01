#![feature(result_option_inspect)]

use crate::days::day1::{day1_a, day1_b};
use crate::wrapper::run_day_preprocess_lines;
use crate::parsers::str_to_opt_i32;

mod wrapper;
mod parsers;

mod days {
    pub(crate) mod day1;
}

fn main() {
    run_day_preprocess_lines("Day 1 A", "res/day1.txt", str_to_opt_i32, day1_a, Option::Some(70613));
    run_day_preprocess_lines("Day 1 B", "res/day1.txt", str_to_opt_i32, day1_b, Option::Some(205805));
}