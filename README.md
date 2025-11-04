# Python Week 2 Workshop: Git Workflow & Code Organization

Welcome! This workshop teaches you how to write clean, well-organized code and collaborate using Git and GitHub.

## 🎯 Learning Goals
- **File Organization**: Learn how to structure your code properly
- **Code Comments & Documentation**: Write clear comments and docstrings
- **Naming Conventions**: Use proper variable and function names
- **Git Workflow**: Save your work early and often with meaningful commits
- **Collaboration**: Create pull requests and see automated tests run

## 📚 Prerequisites
You should know:
- Python variables and operators (+, -, *, /)
- Print statements
- If-else statements
- Basic string operations

## 🚀 Getting Started

### Step 1: Fork This Repository
1. Click the **"Fork"** button at the top-right of this page
2. This creates YOUR own copy of the code
3. You can make changes without affecting the original!

### Step 2: Clone YOUR Fork
Open terminal/command prompt and run:
```bash
# Replace YOUR-USERNAME with your actual GitHub username!
git clone https://github.com/SumitVermakgp/masai-mentor-session-2.git
cd python-week2-workshop
```

**💡 Tip:** Use `pwd` (Mac/Linux) or `cd` (Windows) to check you're in the right folder!

### Step 3: Create Your Working Branch
```bash
git checkout -b fix-bugs
```
**What does this do?** Creates a new "branch" - think of it as your personal workspace where you can experiment safely!

### Step 4: Explore the Code Structure

Take a moment to see how the files are organized:
```
session-2-todo/
├── README.md              ← You are here!
├── exercises/             ← Files you'll fix
│   ├── calculator.py
│   ├── greeting.py
│   └── student_info.py
└── tests/                 ← Tests that run locally
    ├── test_calculator.py
    ├── test_greeting.py
    └── test_student_info.py
```

**📝 Note:** Good file organization makes projects easier to understand and maintain!

## 🔧 Your Tasks

### Exercise 1: Fix calculator.py
**Focus:** Proper naming conventions and clear comments

```bash
# First, let's see what's broken
python exercises/calculator.py
```

**What to fix:**
- Fix the `subtract_numbers()` function (it's adding instead!)
- Complete the `multiply_numbers()` function
- Complete the `divide_numbers()` function (handle division by zero!)
- Fix the `calculate_average()` function (missing a number!)

**💡 Naming Convention Tip:**
- Use `snake_case` for function names (like `calculate_average`)
- Use descriptive names that explain what the function does
- Bad: `calc()`, `func1()`, `x()`
- Good: `calculate_average()`, `add_numbers()`, `get_user_input()`

**After fixing, test it:**
```bash
python exercises/calculator.py
```

**Save your work (commit early!):**
```bash
git add exercises/calculator.py
git commit -m "Fix calculator functions: subtraction and average bugs"
```

**📝 Commit Message Tip:** Write clear commit messages that explain WHAT you fixed and WHY!

---

### Exercise 2: Complete greeting.py
**Focus:** String operations and documentation

```bash
python exercises/greeting.py
```

**What to do:**
- Complete `create_greeting()` function
- Complete `create_goodbye()` function
- Complete `create_introduction()` function
- Fix spacing in `create_welcome_message()` function

**💡 Documentation Tip:**
- Every function should have a docstring (the text in triple quotes)
- Docstrings explain what the function does, parameters, and return values
- Good docstrings help others (and future you!) understand your code

**After fixing:**
```bash
python exercises/greeting.py
git add exercises/greeting.py
git commit -m "Complete greeting functions with proper string formatting"
```

---

### Exercise 3: Fix student_info.py
**Focus:** Logic errors and conditional statements

```bash
python exercises/student_info.py
```

**What to fix:**
- Fix grade assignments in `calculate_grade()` (grades are swapped!)
- Complete `is_passing()` function
- Fix all return values in `get_student_status()` (everything is wrong!)
- Complete `calculate_attendance_status()` function

**💡 Comment Tip:**
- Add comments to explain complex logic
- Don't comment obvious things: `x = 5  # set x to 5` ❌
- Do comment why: `# Calculate percentage to determine attendance status` ✅

**After fixing:**
```bash
python exercises/student_info.py
git add exercises/student_info.py
git commit -m "Fix logic errors in student status functions"
```

---

## 🧪 Testing Your Code

### Run Local Tests
Before pushing, make sure your code works:

```bash
# Test calculator
python tests/test_calculator.py

# Test greeting
python tests/test_greeting.py

# Test student info
python tests/test_student_info.py
```

**💡 "Save Early, Save Often" Tip:**
- Don't wait until everything is perfect to commit!
- Make a commit after each major change
- Small, frequent commits are better than one huge commit
- You can always see your history with: `git log`

---

## 📤 Push Your Changes

When all local tests pass:

```bash
# Push your branch to GitHub
git push origin fix-bugs
```

**What happens now?** Your code goes to YOUR GitHub repository (your fork)!

---

## 🎉 Create a Pull Request

1. Go to YOUR fork on GitHub
2. You'll see a banner saying "Compare & pull request" - click it!
3. Write a description:
   ```
   ## What I Fixed
   - Fixed calculator subtraction bug
   - Completed all greeting functions
   - Fixed student grade logic errors

   ## Testing Done
   - All local tests pass ✓
   - Manually tested each function ✓
   ```
4. Click **"Create pull request"**
5. Watch the automatic tests run! 🤖

**🎊 Surprise!** When you create the PR, hidden tests will run to check edge cases!

---

## ✅ Success Criteria

Your pull request should show:
- [ ] All calculator functions work correctly
- [ ] Greeting functions return proper formatted messages
- [ ] Grade calculator returns correct grades for all scores
- [ ] Student status logic is correct
- [ ] All automatic tests pass (green checkmark ✓)
- [ ] Code follows naming conventions
- [ ] Functions have proper documentation
- [ ] Commit messages are clear and descriptive

---

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Permission denied" when pushing** | Make sure you're pushing to YOUR fork, not the original repo |
| **"git command not found"** | Install Git: https://git-scm.com/downloads |
| **Can't find files** | Check you're in the right directory: `pwd` or `dir` |
| **Tests failing** | Read the error message carefully - it tells you what's wrong! |
| **Forgot to commit** | Use `git status` to see what files changed |
| **Wrong branch** | Use `git branch` to see current branch, `git checkout -b fix-bugs` to create it |

---

## 📖 Git Commands Reference

| Command | What It Does |
|---------|--------------|
| `git status` | Shows which files have changed |
| `git add <file>` | Stages a file for commit |
| `git commit -m "message"` | Saves changes with a description |
| `git push origin <branch>` | Sends your commits to GitHub |
| `git log` | Shows your commit history |
| `git branch` | Shows current branch |
| `git checkout -b <name>` | Creates and switches to new branch |

---

## 🌟 Best Practices You're Learning

### 1. **File Organization**
   - Group related code in appropriate directories
   - Tests go in `tests/` folder
   - Solutions go in `solutions/` folder
   - Keep your project structure clean and logical

### 2. **Code Comments & Documentation**
   - Write docstrings for all functions
   - Add comments to explain WHY, not WHAT
   - Update comments when you change code
   - Use clear, concise language

### 3. **Naming Conventions**
   - Functions: `calculate_average()`, `get_user_name()` (verbs!)
   - Variables: `student_score`, `total_marks` (nouns!)
   - Constants: `MAX_SCORE`, `PASSING_GRADE` (all caps)
   - Be consistent throughout your code

### 4. **Save Early, Save Often**
   - Commit after each logical change
   - Don't wait until "everything is perfect"
   - Write meaningful commit messages
   - Push regularly to backup your work

### 5. **Git Workflow**
   - Create branches for new features
   - Test before pushing
   - Write clear PR descriptions
   - Review your own code before submitting

---

## 🎓 What You've Learned

By completing this workshop, you now know how to:
1. ✅ Fork a repository (make your own copy)
2. ✅ Clone code to your computer
3. ✅ Create branches for your work
4. ✅ Write clean, well-documented code
5. ✅ Follow naming conventions
6. ✅ Make meaningful commits
7. ✅ Push code to GitHub
8. ✅ Create pull requests
9. ✅ Pass automated tests

**Congratulations!** You're now ready to collaborate on real projects! 🚀

---

## 📚 Additional Resources

- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf
- **Python Naming Conventions**: https://pep8.org/#naming-conventions
- **Writing Good Commit Messages**: https://chris.beams.io/posts/git-commit/
- **Python Docstrings**: https://www.python.org/dev/peps/pep-0257/

---

## 🤝 Need Help?

- Ask your peers or mentors first - collaboration is key!
- Review the error messages - they often tell you exactly what's wrong!
- Use `git status` frequently to see what's happening
- Read the comments in the code - they have helpful hints
- Test your code frequently with `python exercises/<filename>.py`

---

## 🎯 Next Steps

After completing this workshop:
1. Create your own Python project
2. Push it to GitHub with proper organization
3. Practice making commits with good messages
4. Help a classmate with their PR!

**Remember:** Good coding practices aren't just about making code work - they're about making code that others (and future you!) can understand and maintain!

Happy coding! 🎉
