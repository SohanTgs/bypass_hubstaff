# ================================================ MOUSAE
# import pyautogui
# import time

# # Move the mouse to specific coordinates
# pyautogui.moveTo(100, 100, duration=1)  # Move mouse to (x, y) in 1 second

# # Perform a click
# pyautogui.click()

# # Drag the mouse
# pyautogui.dragTo(200, 200, duration=1)  # Drag mouse to (x, y) in 1 second

# # Scroll the mouse
# pyautogui.scroll(10)  # Scrolls up

# # Get the current mouse position
# x, y = pyautogui.position()
# print(f"Current mouse position: {x}, {y}")



# ================================================  KEYBOARD
# import pyautogui
# import time

# # Type a string
# pyautogui.typewrite("Hello, world!", interval=0.1)  # Types each character with a 0.1s delay

# # Press and release specific keys
# pyautogui.keyDown('ctrl')
# pyautogui.press('c')
# pyautogui.keyUp('ctrl')

# # Hotkey combinations
# pyautogui.hotkey('ctrl', 'shift', 'esc')  # Simulates pressing Ctrl+Shift+Esc




# Write and mouse move after certain time ================================================ 
# import pyautogui
# import time
# import random
# import string

# # Function for mouse actions
# def perform_mouse_actions():
#     pyautogui.moveTo(100, 100, duration=1)  # Move mouse to (x, y) in 1 second
#     pyautogui.click()
#     pyautogui.dragTo(200, 200, duration=1)  # Drag mouse to (x, y) in 1 second
#     pyautogui.scroll(10)  # Scrolls up
#     x, y = pyautogui.position()
#     print(f"Current mouse position: {x}, {y}")

# # Generate a list of random words
# def generate_random_words():
#     word_count = 10  # Number of random words to generate
#     word_list = []
#     for _ in range(word_count):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
#         word_list.append(word)
#     return word_list

# # Function for keyboard actions
# def perform_keyboard_actions():
#     random_words = generate_random_words()
#     for word in random_words:
#         pyautogui.typewrite(word, interval=0.1)  # Types each character with a 0.1s delay
#         pyautogui.press('space')  # Presses space after each word

# # Run mouse actions and keyboard actions for 2 minutes
# start_time = time.time()
# while time.time() - start_time < 120:  # 120 seconds = 2 minutes
#     perform_mouse_actions()
#     perform_keyboard_actions()






# Work as a human ================================================ 
import pyautogui
import time
import random
import string

# Function for mouse actions
def perform_mouse_actions():
    # Randomly select an action to perform
    actions = [
        lambda: pyautogui.moveTo(random.randint(0, 500), random.randint(0, 500), duration=random.uniform(0.5, 1.5)),
        lambda: pyautogui.click(),
        lambda: pyautogui.dragTo(random.randint(0, 500), random.randint(0, 500), duration=random.uniform(0.5, 1.5)),
        lambda: pyautogui.scroll(random.randint(-100, 100)),  # Scrolls randomly
        lambda: print(f"Current mouse position: {pyautogui.position()}")  # Prints current mouse position
    ]
    random.choice(actions)()  # Perform a randomly selected action

# Generate a list of random words
def generate_random_words():
    word_count = 10  # Number of random words to generate
    word_list = []
    for _ in range(word_count):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
        word_list.append(word)
    return word_list

# Function for keyboard actions
# def perform_keyboard_actions():
#     random_keys = [chr(random.randint(32, 126)) for _ in range(random.randint(5, 15))]  # Random keys to press
#     for$variable = 'value'; key in random_keys:
#         pyautogui.press(key)
#         time.sleep(random.uniform(0.1, 0.5))  # Random delay between key presses

def perform_keyboard_actions():
    # php_code = [
    #     "<?php",
    #     "$variable = 'value';",
    #     "echo 'Hello, PHP!';",
    #     "$array = array(1, 2, 3, 4, 5);",
    #     "for ($i = 0; $i < count($array); $i++) {",
    #     "   echo $array[$i];",
    #     "}",
    #     "$num1 = 10;",
    #     "$num2 = 5;",
    #     "$sum = $num1 + $num2;",
    #     "echo 'The sum is: ' . $sum;",
    #     "$string1 = 'Hello';",
    #     "$string2 = 'World';",
    #     "echo $string1 . ' ' . $string2;",
    #     "// This is a comment in PHP",
    #     "// You can write more comments here",
    #     "function sayHello($name) {",
    #     "   echo 'Hello, ' . $name . '!';",
    #     "}",
    #     "sayHello('John');",
    #     "// End of PHP code",
    #     "// Adding more code here",
    #     "$newVar = 'New Value';",
    #     "echo $newVar;",
    #     "// Another comment",
    #     "for ($j = 0; $j < 3; $j++) {",
    #     "   echo 'Iteration: ' . $j;",
    #     "}",
    # ]

    php_code = [
        "<?php",
        "$variable = 'value';",
        "$another_variable = 10;",
        "function helloWorld() { echo 'Hello, World!'; }",
        "// This is a comment",
        "/* This is a multiline",
        "   comment in PHP */",
        "$array = [1, 2, 3, 4];",
        "$associative_array = ['key' => 'value', 'foo' => 'bar'];",
        "class MyClass { public $property = 'some value'; }",
        "echo 'PHP is powerful';",
        "for ($i = 0; $i < 5; $i++) { echo $i; }",
        "if ($variable == 'value') { echo 'Variable is value'; } else { echo 'Variable is not value'; }",
        "while ($another_variable < 15) { echo $another_variable; $another_variable++; }",
        "switch ($variable) { case 'value': echo 'Value matched'; break; default: echo 'Value not matched'; }",
        "function addNumbers($a, $b) { return $a + $b; }",
        "echo 'This is PHP code'; // You can write PHP here",
        "include 'header.php'; // Including another PHP file",
        "echo 'PHP version: ' . phpversion(); // Getting PHP version",
        "foreach ($array as $element) { echo $element; }",
        "$result = (5 > 3) ? 'Five is greater than three' : 'Five is not greater than three';",
        "/* Escaping characters in strings: \$variable = 'escaped'; */",
        "namespace MyNamespace; // Declaring a namespace",
        "class Car { public function startEngine() { echo 'Engine started'; } }",
        "trait MyTrait { public function doSomething() { echo 'Trait doing something'; } }",
        "echo 'Current date: ' . date('Y-m-d'); // Getting current date",
        "exit(); // Exit PHP execution",
        "die('Script stopped'); // Halt script execution",
        "declare(strict_types=1); // Declaring strict types",
        "function multiplyByTwo(int $num): int { return $num * 2; }",
        "$x = 10; $y = 20; $z = $x + $y; // Adding variables",
        "function concatenateStrings(string ...$strings): string { return implode('', $strings); }",
        "const PI = 3.14; // Defining a constant",
        "use MyNamespace\\MyClass; // Using a class from a different namespace",
        "include_once 'functions.php'; // Including a file once",
        "require 'config.php'; // Requiring a file",
        "echo 'Executing PHP code'; /* Execution starts here */",
        "class Animal { public $type; public function __construct($type) { $this->type = $type; } }",
        "trait MySecondTrait { public function doSomethingElse() { echo 'Trait doing something else'; } }",
        "interface MyInterface { public function myMethod(); }",
        "class Dog extends Animal { public function sound() { echo 'Woof!'; } }",
        "final class FinalClass { /* Cannot be extended */ }",
        "function factorial($n) { return ($n <= 1) ? 1 : $n * factorial($n - 1); }",
        "echo factorial(5); // Output: 120",
        "function divide($a, $b) { if ($b === 0) { throw new Exception('Division by zero'); } return $a / $b; }",
        "try { echo divide(10, 2); /* Output: 5 */ } catch (Exception $e) { echo 'Caught exception: ' . $e->getMessage(); }",
        "function greet($name = 'Guest') { echo 'Hello, ' . $name . '!'; }",
        "greet(); // Output: Hello, Guest!",
        "greet('John'); // Output: Hello, John!",
        "class Rectangle { public $width; public $height; public function __construct($w, $h) { $this->width = $w; $this->height = $h; } public function area() { return $this->width * $this->height; } }",
        "$rect = new Rectangle(5, 10); echo 'Area: ' . $rect->area(); // Output: Area: 50",
        "abstract class Shape { abstract public function area(); }",
        "// Abstract classes cannot be instantiated",
        "class Circle extends Shape { public $radius; public function __construct($r) { $this->radius = $r; } public function area() { return pi() * $this->radius * $this->radius; } }",
        "$circle = new Circle(5); echo 'Circle area: ' . $circle->area(); // Output: Circle area: 78.54",
        "class Singleton { private static $instance; private function __construct() { } public static function getInstance() { if (self::$instance === null) { self::$instance = new Singleton(); } return self::$instance; } }",
        "$singleton = Singleton::getInstance();",
        "echo 'Working with Singleton pattern';",
        "// Do something with the singleton instance...",
        "class User { public $name; public $email; public function __construct($name, $email) { $this->name = $name; $this->email = $email; } }",
        "$user = new User('Alice', 'alice@example.com');",
        "echo 'User: ' . $user->name . ', Email: ' . $user->email;",
        "class Database { private static $instance; private function __construct() { } public static function getInstance() { if (self::$instance === null) { self::$instance = new Database(); } return self::$instance; } public function query($sql) { /* Execute SQL query */ } }",
        "$db = Database::getInstance();",
        "$db->query('SELECT * FROM users');",
        "echo 'Working with Database singleton';",
        "// Perform database operations...",
        "class HTMLHelper { public static function link($url, $text) { return '<a href=\"$url\">$text</a>'; } }",
        "echo HTMLHelper::link('https://example.com', 'Visit Example');",
        "class Logger { public static function log($message) { // Log the message } }",
        "Logger::log('Logging something');",
        "echo 'Using Logger class to log messages';",
        "class Calculator { public static function add($a, $b) { return $a + $b; } public static function subtract($a, $b) { return $a - $b; } }",
        "echo 'Sum: ' . Calculator::add(5, 3) . ', Difference: ' . Calculator::subtract(10, 4);",
    ]

    for line in php_code:
        pyautogui.write(line)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.5, 1.5))  # Add a delay between lines

# Run mouse actions and keyboard actions for 2 minutes
start_time = time.time()
while time.time() - start_time < 1000000: 
# while time.time() - start_time < 120:  # 120 seconds = 2 minutes
    perform_mouse_actions()
    perform_keyboard_actions()
