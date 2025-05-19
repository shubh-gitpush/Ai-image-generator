# Image Generation App

<p style="font-size:16px; color:#555;">
This project lets users generate AI images from text prompts using a React frontend and Django backend.  
It includes Docker support and GitHub Actions for CI/CD automation.
</p>

<h2 style="color:#1a73e8;">How It Works</h2>
<p style="font-size:14px; color:#333;">
Users first <strong>log in</strong> to the app. After authentication, they can enter a text prompt to generate an AI image.  
The backend sends the prompt to the Stability AI API, receives a generated image, and sends it back to the frontend, which displays it dynamically.
</p>

<h2 style="color:#1a73e8;">Login Process</h2>
<ul style="font-size:14px; color:#333;">
  <li>Visit the login page.</li>
  <li>Enter your username/email and password.</li>
  <li>Submit the form to authenticate.</li>
  <li>Upon success, access the image generation form.</li>
</ul>

<h2 style="color:#1a73e8;">Docker Support</h2>
<p style="font-size:14px; color:#333;">
The project includes a <code>Dockerfile</code> to containerize the app for easy deployment.  
Simply build the Docker image with <code>docker build</code> and run the container to start the backend server.
</p>

<h2 style="color:#1a73e8;">GitHub Actions (CI/CD)</h2>
<p style="font-size:14px; color:#333;">
A GitHub Actions workflow (<code>.github/workflows/ci.yml</code>) runs tests automatically on every push or pull request.  
This helps ensure code quality and streamline deployment.
</p>

<h2 style="color:#1a73e8;">Environment Variables</h2>
<p style="font-size:14px; color:#333;">
Make sure to add your API keys in a <code>.env</code> file or environment, including:<br/>
<strong>STABILITY_API_KEY</strong> and <strong>DJANGO_SECRET_KEY</strong>.
</p>

<hr>
<h2 style="color:#1a73e8;"> screenshot</h2>

<img src="/img.png"></img>


---

<p style="font-size:12px; color:#777; text-align:center; margin-top:40px;">
Thank you for checking out this project! 🌟  
Feel free to open issues or contribute.
</p>
