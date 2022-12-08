use std::cmp;
use std::collections::HashMap;
use std::cell::RefCell;
use std::rc::Rc;

pub fn solve() {
    let root = Rc::new(RefCell::new(Directory::new()));

    let mut current = Rc::clone(&root); 
    include_str!("../inputs/dec07.txt")
        .lines()
        .skip(1)
        .for_each(|line| {
            if line.starts_with("$ cd") {
                let mut split = line.split_whitespace();
                split.next();
                split.next();
                let path = split.next().unwrap().to_string();

                if current.borrow().sub_directories.contains_key(&path) {
                    let cd_to = Rc::clone(current.borrow().sub_directories.get(&path).unwrap());
                    current = cd_to
                } else {
                    let new =  Rc::new(RefCell::new(Directory::new()));
                    new.borrow_mut().add_sub_directory("..".to_string(), Rc::clone(&current));
                    current.borrow_mut().add_sub_directory(path, Rc::clone(&new));

                    current = new;
                }
            } else if line.chars().next().unwrap().is_numeric() {
                let mut split = line.split_whitespace();
                let size = split.next().unwrap().parse::<u32>().unwrap();
                let name = split.next().unwrap();

                let file = Rc::new(RefCell::new(File { size }));
                current.borrow_mut().add_file(name.to_string(), Rc::clone(&file));
            }
        });

    root.borrow_mut().calculate_dir_sizes();
    
    println!("--- Part One ---");
    println!("{}", sum_of_dirs_under_size(Rc::clone(&root), 100000));

    println!("--- Part Two ---");
    let space_to_free = 30000000 + root.borrow().size.unwrap() - 70000000;
    println!("{}", least_over_val(root, space_to_free));
}

struct File {
    size: u32
}

struct Directory {
    size: Option<u32>,
    sub_directories: HashMap<String, Rc<RefCell<Directory>>>,
    files: HashMap<String, Rc<RefCell<File>>>
}

impl Directory {
    fn new() -> Directory {
      Directory {
        size: None,
        sub_directories: HashMap::new(),
        files: HashMap::new()
      }
    }

    fn add_sub_directory(&mut self, name: String, directory: Rc<RefCell<Directory>>) {
      self.sub_directories.insert(name, directory);
    }
    
    fn add_file(&mut self, name: String, file: Rc<RefCell<File>>) {
      self.files.insert(name, file);
    }

    fn calculate_dir_sizes(&mut self) -> u32 {
        let sub_directory_size_sum: u32 = self
            .sub_directories
            .iter()
            .filter(|(name, _)| name != &"..")
            .map(|(_, dir_ref)| dir_ref.borrow_mut().calculate_dir_sizes())
            .sum();

        let file_size_sum: u32 = self
            .files
            .iter()
            .map(|(_, file_ref)| file_ref.borrow().size)
            .sum();

        self.size = Some(file_size_sum + sub_directory_size_sum);
        file_size_sum + sub_directory_size_sum
    }
}

fn sum_of_dirs_under_size(dir_ref: Rc<RefCell<Directory>>, val: u32) -> u32 {
    let directory = dir_ref.borrow();

    let size_of_sub_dirs = directory
        .sub_directories
        .iter()
        .filter(|(name, _)| name != &"..")
        .map(|(_, dir_ref)| sum_of_dirs_under_size(Rc::clone(dir_ref), val))
        .sum();

    if directory.size.unwrap() > val {
        return size_of_sub_dirs;
    }

    size_of_sub_dirs + directory.size.unwrap()
}

fn least_over_val(dir_ref: Rc<RefCell<Directory>>, val: u32) -> u32 {
    let directory = dir_ref.borrow();
    
    if directory.size.unwrap() < val {
        return u32::MAX;
    }

    let mut least_so_far = u32::MAX;
    if directory.size.unwrap() >= val {
        least_so_far = directory.size.unwrap();
    }
    
    cmp::min(least_so_far, directory
        .sub_directories
        .iter()
        .filter(|(name, _)| name != &"..")
        .map(|(_, dir_ref)| least_over_val(Rc::clone(dir_ref), val))
        .min().unwrap()
    )
}
