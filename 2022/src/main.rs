use std::env;
use std::process;

mod dec01;

fn main() {
    if env::args().len() != 2 {
        println!("Usage: cargo run <day>");
        process::exit(1);
    } 
    let day = env::args().last().unwrap();

    match day.as_ref() {
        "dec01" => dec01::solve(),
        _ => println!("No solution for {}", day),
    };
}
