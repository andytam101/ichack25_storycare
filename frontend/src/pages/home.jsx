import { useState } from "react";
import { Box, Typography, TextField, Container, Button } from "@mui/material";
import StoryViewer from "./storyviewer"; // Import the story viewer

export default function Home() {
    const [prompt, setPrompt] = useState("");
    const [prompt2, setPrompt2] = useState("");
    const [submittedPrompt, setSubmittedPrompt] = useState(null);
    const [submittedPrompt2, setSubmittedPrompt2] = useState(null);
    const [isVisible2, setIsVisible2] = useState(false);
    const [submittedType, setSubmittedType] = useState(null);
    const [selectedType, setSelectedType] = useState("");

    const handleSearch = (event) => {
        if (event.key === "Enter" || event.type === "click") {
            setSubmittedPrompt(prompt); // Send prompt to StoryViewer
            setSubmittedPrompt2(prompt2);
            setSubmittedType(selectedType);
        }
    };

    const handleTypeChange = e => {
        let value = e.target.value
        setSelectedType(e.target.value)
        if (value === "test") {
            setIsVisible2(false);
            document.getElementById("textfield").setAttribute("placeholder", "Enter a medical test...");
        } else if (value === "treatment") {
            setIsVisible2(true);
        } else {
            setIsVisible2(false);
            document.getElementById("textfield").setAttribute("placeholder", "Enter a disease...");
        }
    }

    return (
        <>
            {!submittedPrompt ? (
                // Home Page with Search Bar
                <Container maxWidth="sm">
                    <Box
                        display="flex"
                        flexDirection="column"
                        alignItems="center"
                        justifyContent="center"
                        height="100vh"
                        textAlign="center"
                    >
                        <Typography variant="h2" gutterBottom>
                            StoryCare
                        </Typography>
                        <Typography variant="h6" color="textSecondary" gutterBottom>
                            Your story, your strength.
                        </Typography>
                        <div value={selectedType}>
                            <label>Type: </label>
                            <select value={selectedType} onChange={handleTypeChange}>
                                <option value="">-- Choose --</option>
                                <option value="test">Medical Test</option>
                                <option value="diagnosis">Diagnosis</option>
                                <option value="day_in_life">Day In The Life</option>
                                <option value="treatment">Treatment</option>
                                <option value="red_flags">Watch Out For</option>
                            </select>
                        </div>
                        <TextField
                            variant="outlined"
                            placeholder="Enter a disease..."
                            fullWidth
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            onKeyDown={handleSearch}
                            id="textfield"
                            sx={{ mt: 2 }}
                        />
                        <TextField
                            variant="outlined"
                            placeholder="Enter a treatment..."
                            fullWidth
                            value={prompt2}
                            onChange={(e) => setPrompt2(e.target.value)}
                            onKeyDown={handleSearch}
                            id="textfield2"
                            sx={{ mt: 2 }}
                            style={{ display: isVisible2 ? "block" : "none" }}
                        />
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSearch}
                            sx={{ mt: 2 }}
                        >
                            Generate Story
                        </Button>
                    </Box>
                </Container>
            ) : (
                // Show StoryViewer when the user submits a search
                <StoryViewer prompt={submittedPrompt} prompt2={submittedPrompt2} promptType={submittedType}/>
            )}
        </>
    );
}

