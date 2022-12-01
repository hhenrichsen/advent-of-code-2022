#![feature(result_option_inspect)]

use crate::days::day1::{day1_a, day1_b};
use crate::wrapper::{prep_opt_i32, run_day};

mod wrapper;

mod days {
    pub(crate) mod day1;
}

fn main() {
    run_day("Day 1 A", "res/day1.txt", prep_opt_i32, day1_a, Option::Some(70613));
    run_day("Day 1 B", "res/day1.txt", prep_opt_i32, day1_b, Option::Some(205805));
}