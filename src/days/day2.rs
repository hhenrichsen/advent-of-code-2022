use std::collections::HashMap;

use lazy_static::lazy_static;

use crate::parsers::split_string_into_pair;

lazy_static! {
    static ref BEATS: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("Y", "A");
        m.insert("Z", "B");
        m.insert("X", "C");
        m
    };
    
    static ref BEATS_REVERSED: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("A", "Y");
        m.insert("B", "Z");
        m.insert("C", "X");
        m
    };


    static ref LOSES: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("A", "Z");
        m.insert("B", "X");
        m.insert("C", "Y");
        m
    };

    static ref A_TO_Z: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("A", "X");
        m.insert("B", "Y");
        m.insert("C", "Z");
        m
    };

    static ref Z_TO_A: HashMap<&'static str, &'static str> = {
        let mut m = HashMap::new();
        m.insert("X", "A");
        m.insert("Y", "B");
        m.insert("Z", "C");
        m
    };

    static ref SCORES: HashMap<&'static str, i32> = {
        let mut m = HashMap::new();
        m.insert("X", 1);
        m.insert("Y", 2);
        m.insert("Z", 3);
        m
    };
}

pub(crate) fn day2_a(input: &[&str]) -> i32 {
    input.into_iter().map(|line| {
        let (a, b) = split_string_into_pair(line);
        let res = if BEATS.get(b).unwrap().eq_ignore_ascii_case(a) {
            6
        }
        else if *Z_TO_A.get(b).unwrap() == a {
            3
        }
        else {
            0
        } + SCORES.get(b).unwrap();
        return res;
    }).sum()
}

pub(crate) fn day2_b(input: &[&str]) -> i32 {
    input.into_iter().map(|line| {
        let (a, b) = split_string_into_pair(line);
        if b == "X" {
            SCORES.get(LOSES.get(a).unwrap()).unwrap() + 0
        }
        else if b == "Y" { 
            SCORES.get(A_TO_Z.get(a).unwrap()).unwrap() + 3
        }
        else {
            SCORES.get(BEATS_REVERSED.get(a).unwrap()).unwrap() + 6
        }
    }).sum()
}