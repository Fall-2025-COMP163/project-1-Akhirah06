[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21303849&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations. The project is based on a fantasy RPG that takes on elements of the well known anime “Frieren: Beyond Journey’s End” with side elements of its own. It consists of classes: Base, Combatant, Sorcerer, Mischief, Shootaz, Glitchez, and Hybrid. Hybrids, Glitchez, and Shootaz are the strongest classes to be born into in my RPG game. The stats did formulate based on the example provided at the start before I started coding. However, since the Hybrids, Glitchez, and Shootaz classes are the strongest classes they were given stronger stats; the catch is that stronger the class, the higher the rarity to be born into it. Now for the leveling system, I put it into this kind of system: High “stat” = (level x 10), Medium “stat” = (level x 7), and Low “stat” = (level x 3). I don’t think I added anything specifically unique, but when I was making the code for it to work I made another function to make filename a global variable. I did end up using ChatGPT for this project to assist with syntax formatting. The areas that have AI assistance in it are in the functions “def load_character” and “def display_character”. To run the code, you enter your character’s name and what class you want them to be born into. After that, you add what level they are then it calculates what their stats will become. 


# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge
