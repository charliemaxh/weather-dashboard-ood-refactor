# Weather Dashboard OOD Template

This repository serves as a template for teaching Object-Oriented Design (OOD) principles in Python through a Weather Dashboard application. It provides a high-level design, skeleton code, and a step-by-step implementation strategy to help students understand the big picture and the motivation behind incremental changes.

## How to Use This Template

To use this template:

1. Click the "Use this template" button at the top of the repository page.
2. Create a new repository based on this template.
3. Clone your new repository to your local machine:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

4. Create a Python virtual environment:
   - For Windows:
     ```
     python -m venv venv
     ```
   - For macOS and Linux:
     ```
     python3 -m venv venv
     ```

5. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

7. Set up your API key:
   - Copy the `env.example` file to `.env`:
     ```
     cp env.example .env
     ```
   - Open the `.env` file and replace `YOUR_API_KEY_HERE` with your actual OpenWeatherMap API key.

8. You're now ready to start working on the project! Follow the implementation steps outlined in the documentation.

**Note:** We recommend using the "Use this template" button rather than cloning the repository directly. This ensures you have your own copy to work with and can easily track your progress.

To deactivate the virtual environment when you're done working on the project, simply run:
```
deactivate
```

Remember to activate the virtual environment each time you work on the project to ensure you're using the correct dependencies.

## Required Python Modules

This project requires the following Python modules:

- requests
- python-dotenv
- matplotlib

These are already listed in the `requirements.txt` file and will be installed when you follow the setup instructions above.

## API Key Management

This project uses the OpenWeatherMap API. To use this API, you need to sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api).

Once you have your API key, add it to the `.env` file as described in step 7 of the setup instructions.

To use the API key in your code, you can do the following:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENWEATHERMAP_API_KEY")
```

This code snippet should be added at the beginning of your main script or in the `__init__` method of your `WeatherAPI` class.

## Repository Structure

- `src/`: Contains the source code for the Weather Dashboard application
- `docs/`: Includes detailed documentation on the design and implementation steps
- `tests/`: Contains unit tests for the application components
- `requirements.txt`: Lists the Python dependencies for the project
- `env.example`: Example environment file for API key management

## Getting Started

1. Review the high-level design document in the `docs/` folder.
2. Familiarise yourself with the skeleton code in the `src/` directory.
3. Follow the step-by-step implementation guide in the documentation.
4. Run the tests in the `tests/` directory to verify your implementation.

## Contributing

This template is designed for educational purposes. If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

We hope this template helps you gain a better understanding of Object-Oriented Design principles and their application in real-world scenarios