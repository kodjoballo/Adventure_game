# 🗡️ Adventure Game

## 📌 Description
This is a **text-based adventure game** where you, the player, navigate through a mysterious land by making choices.  
Your decisions lead to different story outcomes — you might **win glory** 🎉 or face a **grim defeat** 💀.  

The game loads its storyline from a `story.json` file, allowing flexible branching paths and endings.  

---

## 🚀 How to Run

### 1. Ensure you have Python 3 installed
Check with:
```js
python --version


```

Either run the code via cmd while being in the directory with python.exe advendure_game.py or using an interpreter


<p align="center">

![image alt](https://github.com/kodjoballo/Adventure_game/blob/main/adventure_game.png?raw=true)

</p>


### 2. File structure
```js
adventure_game/
│
├── adventure_game.py          # main Python script
├── data/story.json       # JSON file with story nodes & branching
└── assets/
```

### 3. 📖 Story JSON Format

The story.json file contains the branching story structure.
```js
Example:

{
  "1": {
    "text": "You wake up in a dark forest. Do you pick up the sword?",
    "A": 2,
    "B": "LOSE"
  },
  "2": {
    "text": "You hear footsteps. Do you fight or hide?",
    "A": "WIN",
    "B": "LOSE"
  }
}
```

### 4. 📚 Concepts Used

File I/O with json

Error handling (try/except for missing files or permissions)

Data structures (dictionary-based branching system)

User input & validation

Game loop mechanics


### 5. 🌟 Future Enhancements

Add more branching paths and storylines

Allow saving and loading game progress

Add colored text for choices and outcomes

### 6. Code source below

[code_source](https://github.com/kodjoballo/Adventure_game/blob/main/adventure_game.py)


