use std::fmt::Display;
use std::fs;
use colored::Colorize;

fn check_result<Res: Display + PartialEq>(title: &'static str, expected: Option<Res>, res: Res) {
    println!("{} Result: {}", title, res);
    if expected.is_some() {
        let test = expected.unwrap();
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
/// * `Res` - The result from this problem, something to display.
/// * `Input` - The type of input the problem function is expecting.
/// * `Prep` - The transformation from input line to the input the problem is expecting.
/// * `Problem` - The problem function.
///
pub fn run_day<Res, Input, Prep, Problem>(title: &'static str, name: &'static str, prep: Prep, prob: Problem, expected: Option<Res>)
    where Res: Display + PartialEq,
          Prep: Fn(&str) -> Input,
          Problem: Fn(&[Input]) -> Res {

    let raw_contents = fs::read_to_string(name).expect(&*format!("Failed to read {}", name));
    let contents = raw_contents.lines().collect::<Vec<&str>>();
    let transformed: Vec<Input> = contents.into_iter().map(prep).collect();

    let res = prob(transformed.as_slice());
    check_result(title, expected, res);
}

pub fn run_day_no_prep<Res, Problem>(title: &'static str, name: &'static str, prob: Problem, expected: Option<Res>)
    where Res: Display + PartialEq,
          Problem: Fn(&[&str]) -> Res {

    let raw_contents = fs::read_to_string(name).expect(&*format!("Failed to read {}", name));
    let contents = raw_contents.lines().collect::<Vec<&str>>();

    let res = prob(contents.as_slice());
    check_result(title, expected, res);
}

pub fn prep_opt_i32(line: &str) -> Option<i32> {
    line.parse::<i32>().ok()
}

/// Quick conversion function from str to i32
pub fn prep_i32(line: &str) -> i32 {
    line.parse::<i32>().expect(line)
}