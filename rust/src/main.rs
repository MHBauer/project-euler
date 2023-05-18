fn main() {
    println!("{}", euler1());
}

fn euler1() -> u64{
    let mut acc = 0;
    for i in 3..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            acc += i
        }
    }
    acc
}
