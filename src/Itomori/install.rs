use std::process::Command;

fn main() {
    let status = Command::new("uv")
        .arg("tool")
        .arg("install")
        .arg("git+https://github.com/TheAhumMaitra/Itomori.git")
        .status()
        .expect("Failed to execute command");

    println!("Command exited with: {}", status);
}
