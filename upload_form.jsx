import React, { useState } from 'react';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInput = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    const formData = new FormData();
    formData.append('file', selectedFile);
    // Add additional API calls here to upload the file data
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Upload Data</h1>
      </header>
      <div>
        <input type="file" onChange={handleFileInput} />
        <button onClick={handleFileUpload}>Upload</button>
      </div>
    </div>
  );
}

export default App;
// In this example, the useState hook is used to manage the state of the selected file. The handleFileInput function is triggered when a file is selected, and sets the selected file state. The handleFileUpload function is triggered when the "Upload" button is clicked, and creates a new FormData object to send the selected file to an API endpoint.

// You can customize the styling of the component as needed to match your design preferences.





