
use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() {
    let part_one = part_one();
    let part_two = part_two();

    println!("{}", part_one);
    println!("{}", part_two);

}

fn get_lines() -> Vec<u32> {

    let filename = "input.txt";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    return reader.lines().map(|x| x.unwrap().trim().parse::<u32>().unwrap()).collect();
}


pub fn part_one() -> u32 {
    let mut counter:
    u32 = 0;
    let vec = get_lines();
    for (i, _) in vec.iter().enumerate() {
        if i == 0 {
            continue;
        }

        if vec[i - 1] < vec[i] {
            counter += 1;
        }
    }

    return counter;
}

pub fn part_two() -> u32 {
    let vec = get_lines();
    let mut counter: u32 = 0;
    let mut prev = u32::MAX;

    for window in vec.windows(3) {
        let cur: u32 = window.iter().sum();
        if cur > prev {
            counter += 1;
        }
        prev = cur;
    }

    return counter;
}
