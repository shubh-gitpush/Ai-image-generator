import React, { useState } from 'react';//use state is react hook that lets you add states of data
import axios from 'axios'; //http request like post get

function PromptForm() {
  const [prompt, setPrompt] = useState('');
  const [imageBase64, setImageBase64] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();  //stops the browser from loading the page when clicked on generated
    setLoading(true);   //disable the form and start loading
    try {
      const res = await axios.post('http://localhost:8000/api/generate/', { prompt }); //send post request to django
      setImageBase64(res.data.image_base64);//save the image to state
    } catch (err) {
      alert('Image generation failed.');  //for error
    } finally {
      setLoading(false);  //reset after a request is complete weather error or nit
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter image prompt"
          value={prompt}//controlled by prompt state
          onChange={(e) => setPrompt(e.target.value)}//update as user types
          disabled={loading}//disable input while loading
        />
        <button type="submit" disabled={loading || !prompt.trim()}>//disbale if prompt is empty
          {loading ? 'Generating...' : 'Generate Image'}
        </button>
      </form>
      {imageBase64 && (
        <div style={{ marginTop: '20px' }}>
          <img
            src={`data:image/png;base64,${imageBase64}`}
            alt="Generated"
            style={{ maxWidth: '100%' }}
          />
        </div>
      )}
    </div>
  );
}

export default PromptForm;
