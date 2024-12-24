**NAME:** SHAIK MOHAMMAD IRFAN  
**COMPANY:** CODTECH IT SOLUTIONS  
**ID:** CT08DS395  
**DOMAIN:** Cyber Security and Ethical Hacking  
**Duration:** December 2024 to January 2025  


# Password Strength Checker

## Description
This tool evaluates the strength of user passwords based on factors like length, character diversity, and uniqueness. 
It provides real-time feedback on password quality and offers suggestions for improvement if the password is weak. 
Additionally, it can generate strong passwords with a combination of uppercase letters, lowercase letters, 
numbers, and special characters.

---

## Features
1. **Password Analysis**:
   - Evaluates password length.
   - Checks for uppercase, lowercase, numbers, and special characters.
   - Detects repeated characters for uniqueness.

2. **Feedback**:
   - Categorizes passwords as Weak, Moderate, or Strong.
   - Provides detailed suggestions to improve weak passwords.

3. **Advanced Features**:
   - Strong password generator.
   - Optional GUI or web interface for better user interaction.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `re` - For regular expressions and pattern matching.
  - `random` - For generating random passwords.
  - `string` - For character operations.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd password-strength-checker
   ```

2. **Run the Script**:
   ```bash
   python password_strength_checker.py
   ```

3. **Features**:
   - Input a password when prompted to check its strength.
   - View suggestions for improvement if the password is weak.
   - Use the built-in password generator for a strong password.

---

## File Structure
- `password_strength_checker.py`: Main script for password strength evaluation.
- `README.md`: Documentation for the project.

---

## Sample Output
**Strong Password**:
```plaintext
Enter your password: Pa$$w0rd123
Password Strength: Strong
```

**Weak Password**:
```plaintext
Enter your password: abc123
Password Strength: Weak
Suggestions:
1. Increase length to at least 8 characters.
2. Add at least one uppercase letter.
3. Include at least one special character.
Generated Strong Password: Xj8@cB$M4Lz!
```

---

## Future Enhancements
- Add a graphical user interface (GUI) using Tkinter or Flask.
- Implement entropy-based scoring for more accurate analysis.
- Add real-time typing feedback for password strength.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author
[SHAIK MOHAMMAD IRFAN](https://github.com/irfan2607)
