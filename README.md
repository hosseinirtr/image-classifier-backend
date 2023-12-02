# Image Classifier Project

## Description

This project is a Django-based application that allows users to upload images. These images are then classified using a machine learning model, specifically the InceptionResNetV2 model.

## Installation

1. Clone this repository to your local machine.

2. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django migrations to set up your database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to the running server (usually `localhost:8000`).

3. You will see a form to upload an image. Click on the "Choose File" button and select an image from your computer.

4. After selecting an image, click on the "Upload" button to upload the image.

5. The application will classify the image and display the result on the page.

## Contributing

Contributions are welcome. Please submit a pull request or open an issue if you have something to contribute.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
