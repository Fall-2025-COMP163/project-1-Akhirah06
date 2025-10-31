# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: [Akhirah Henry]
# Date: [October 27, 2025]

AI Usage: [ChatGPT]
AI helped with file I/O error handling logic in display_character function and load_character function.


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1  # Starting level 
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100  # Starting gold
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Combatants: High strength, low magic, high health
    - Sorcerers: Low strength, high magic, medium health  
    - Mischiefs: Medium strength, medium magic, low health
    - Shootaz: Medium strength, high magic, high health
    - Glitchez: High strength, medium magic, high health
    - Hybrids: High strength, high magic, high health
    """
    character_class = character_class.title()
    if character_class == "Combatant":
        strength = 10 + (level * 10)
        magic = 2 + (level * 3)
        health = 100 + (level * 10)
    elif character_class == "Sorcerer":
        strength = 4 + (level * 3)
        magic = 12 + (level * 10)
        health = 80 + (level * 7)
    elif character_class == "Mischief":
        strength = 7 + (level * 7)
        magic = 7 + (level * 7)
        health = 70 + (level * 3)
    elif character_class == "Shootaz":
        strength = 7 + (level * 7)
        magic = 12 + (level * 10)
        health = 100 + (level * 10)
    elif character_class == "Glitchez":
        strength = 12 + (level * 10)
        magic = 7 + (level * 7)
        health = 100 + (level * 10)
    elif character_class == "Hybrid":
        strength = 10 + (level * 10)
        magic = 10 + (level * 10)
        health = 100 + (level * 10)
    else:
        # Default stats for base class
        strength = 5
        magic = 5
        health = 90
    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(filename, "w") as character_file:
        character_file.write("Character Name: " + character["name"])
        character_file.write("\n")
        character_file.write("Class: " + character["class"])
        character_file.write("\n")
        character_file.write("Level: " + str(character["level"]))
        character_file.write("\n")
        character_file.write("Strength: " + str(character["strength"]))
        character_file.write("\n")
        character_file.write("Magic: " + str(character["magic"]))
        character_file.write("\n")
        character_file.write("Health: " + str(character["health"]))
        character_file.write("\n")
        character_file.write("Gold: " + str(character["gold"]))
        character_file.write("\n")
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    with open(filename, "r") as character_file:
        lines = character_file.readlines()
        character = {}
        for line in lines:
            key, values = line.strip().split(": ")
            key = key.lower().replace("character name", "name")
            if key in ["level", "strength", "magic", "health", "gold"]:
                values = int(values)
            character[key] = values
    return character

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    for key, value in character.items():
        print(f"{key}: {value}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] += 1
    save_character(character, character["name"])
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    save_character(character, filename(character))

def filename(character):
    filename = character["name"] + ".txt"
    return filename

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    char = create_character("Asta", "Glitchez")
    char["level"] = int(input())
    char["strength"], char["magic"], char["health"] = calculate_stats("Glitchez", char["level"])
    save_character(char, filename(char))
    char = load_character(filename(char))
    display_character(char)
    # Should be: {name: Asta, class: Glitchez, level: 20, strength: 152, magic: 147, health: 300, gold: 100}
   