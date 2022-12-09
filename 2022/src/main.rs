extern crate regex;

use std::env;
use std::process;

mod dec01;
mod dec02;
mod dec03;
mod dec04;
mod dec05;
mod dec06;
mod dec07;
mod dec08;
mod dec09;

fn main() {
    if env::args().len() != 2 {
        println!("Usage: cargo run <day>");
        process::exit(1);
    } 
    let day = env::args().last().unwrap();

    match day.as_ref() {
        "dec01" => dec01::solve(),
        "dec02" => dec02::solve(),
        "dec03" => dec03::solve(),
        "dec04" => dec04::solve(),
        "dec05" => dec05::solve(),
        "dec06" => dec06::solve(),
        "dec07" => dec07::solve(),
        "dec08" => dec08::solve(),
        "dec09" => dec09::solve(),
        _ => println!("No solution for {}", day),
    };
}