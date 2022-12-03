#![allow(dead_code)]

use std::fmt::Display;
use std::fs;
use colored::Colorize;

fn check_result<Res: Display + PartialEq>(title: &'static str, expected: Option<Res>, res: Res) {
    println!("{} Result: {}", title, res);
    if let Some(test) = expected {
        if test == res {
            println!("{}", "\tPASS".green());
            println!();
        }
        else {
            println!("{}", "\tFAIL".red());
            println!();
        }
    }
}

/// Runs a day's problem.
///
/// # Arguments
/// * `title` - The name of the day.
/// * `name` - The name of the file to read.
/// * `prep` - The mapping function to convert lines of input to the input the problem is expecting.
/// * `prob` - The problem function.
///
/// # Generic Types
/// * `Result` - The result from this problem, something to display.
/// * `Input` - The type of input the problem function is expecting.
/// * `LineProcessor` - The transformation from input line to the input the problem is expecting.
/// * `Problem` - The problem function.
///
pub fn run_day_preprocess_lines<Result, Input, LineProcessor, Problem>(title: &'static str, name: &'static str, line_processor: LineProcessor, problem: Problem, expected: Option<Result>)
    where Result: Display + PartialEq,
          LineProcessor: Fn(&str) -> Input,
          Problem: Fn(&[Input]) -> Result {

    let input : Vec<Input> = fs::read_to_string(name)
        .unwrap_or_else(|_| panic!("Failed to read {}", name))
        .lines()
        .map(line_processor).collect();

    let res = problem(input.as_slice());
    check_result(title, expected, res);
}

pub fn run_day_preprocess_full_input<Result, Input, Preprocessor, Problem>(title: &'static str, name: &'static str, preprocessor: Preprocessor, problem: Problem, expected: Option<Result>)
    where Result: Display + PartialEq,
          Preprocessor: Fn(Vec<&str>) -> Input,
          Problem: Fn(&Input) -> Result {

    let input = preprocessor(
        fs::read_to_string(name)
            .unwrap_or_else(|_| panic!("Failed to read {}", name))
            .lines()
            .collect()
    );

    let res = problem(&input);
    check_result(title, expected, res);
}

pub fn run_day_raw_lines<Result, Problem>(title: &'static str, name: &'static str, problem: Problem, expected: Option<Result>)
    where Result: Display + PartialEq,
          Problem: Fn(&[&str]) -> Result {

    let raw_contents = fs::read_to_string(name).unwrap_or_else(|_| panic!("Failed to read {}", name));
    let contents : Vec<&str> = raw_contents.lines().collect();

    let res = problem(contents.as_slice());
    check_result(title, expected, res);
}