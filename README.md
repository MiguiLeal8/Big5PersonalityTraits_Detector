# Big5PersonalityTraits_Detector
## Overview
The Big5PersonalityTraits_Detector is a project designed to analyze text and determine the Big Five personality traits of the author. The Big Five personality traits are Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.
The model for emotion detector in text is a model trained from roberta-base on the go_emotions dataset for multi-label classification, from [SamLowe/roberta-base-go_emotions] (https://huggingface.co/SamLowe/roberta-base-go_emotions)

## Features
- Initial BFI-44 test for the initial personality
- Analyze text to detect personality traits
- Generate a detailed report of the personality analysis
- Show goals for your mental health
- Easy to use and integrate into other projects

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To use the Big5PersonalityTraits_Detector, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/miguileal8/Big5PersonalityTraits_Detector.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Big5PersonalityTraits_Detector
    ```
3. Run the main script:
    ```bash
    python3 main.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please contact [miguileal8](mailto:miguileal8@gmail.com).