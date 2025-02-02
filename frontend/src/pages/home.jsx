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
    const [username, setUsername] = useState("");
    const [submittedUsername, setSubmittedUsername] = useState(null);

    const handleSearch = (event) => {
        if (event.key === "Enter" || event.type === "click") {
            setSubmittedPrompt(prompt); // Send prompt to StoryViewer
            setSubmittedPrompt2(prompt2);
            setSubmittedType(selectedType);
            setSubmittedUsername(username);
        }
    };

    const handleTypeChange = (e) => {
        let value = e.target.value;
        setSelectedType(value);
        if (value === "test") {
            setIsVisible2(false);
            document.getElementById("textfield").setAttribute("placeholder", "Enter a medical test");
        } else if (value === "treatment") {
            setIsVisible2(true);
        } else {
            setIsVisible2(false);
            document.getElementById("textfield").setAttribute("placeholder", "Enter the medical condition");
        }
    };

    return (
        <>
            {!submittedPrompt ? (
                // Home Page with Search Bar
                <Container maxWidth="sm" sx={{ display: "flex", justifyContent: "center", height: "100vh" }}>
                    <Box
                        display="flex"
                        flexDirection="column"
                        alignItems="center"
                        justifyContent="center"
                        textAlign="center"
                        sx={{
                            backgroundColor: "white",
                            borderRadius: "16px",
                            padding: "24px",
                            boxShadow: 3,
                            width: "100%",
                            maxWidth: "500px",
                            marginTop: "6vh",
                            marginBottom: "30px"
                        }}
                    >
                        <div marginBottom="12px" style={{ marginTop: "-36px"}}>
                            <img src="/book.png" alt="Picture of a book." height="96px"/>                
                        </div>
                        <Typography variant="h2" marginTop="4vh" marginBottom="6px" gutterBottom sx={{ fontWeight: 700 }}>
                            StoryCare
                        </Typography>
                        <Typography variant="h6" color="textSecondary" gutterBottom marginBottom="24px" sx={{
                            animation: "floatIn 2s ease-out forwards",
                        }}>
                            One story at a time.
                        </Typography>
                        
                        {/* Type label and dropdown on the same line */}
                        <Box sx={{ display: "flex", alignItems: "center", mb: 2 }}>
                            <label style={{ fontSize: "16px", fontWeight: 500, marginRight: "12px" }}>Choose Story Type:</label>
                            <select
                                value={selectedType}
                                onChange={handleTypeChange}
                                style={{
                                    padding: "8px",
                                    fontSize: "16px",
                                    width: "200px",
                                    borderRadius: "8px",
                                    border: "1px solid #ccc",
                                }}
                            >
                                <option value="">-- Choose --</option>
                                <option value="test">Medical Test</option>
                                <option value="diagnosis">Diagnosis</option>
                                <option value="day_in_life">Day In The Life</option>
                                <option value="treatment">Treatment</option>
                                <option value="red_flags">Watch Out For</option>
                            </select>
                        </Box>

                        <TextField
                            variant="outlined"
                            placeholder="Enter the character's name"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            onKeyDown={handleSearch}
                            fullWidth
                            sx={{ mt: 2, width: "90%" }}
                        />
                        <TextField
                            variant="outlined"
                            placeholder="Enter the medical condition"
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            onKeyDown={handleSearch}
                            id="textfield"
                            fullWidth
                            sx={{ mt: 2, width: "90%" }}
                        />
                        <TextField
                            variant="outlined"
                            placeholder="Enter a treatment"
                            value={prompt2}
                            onChange={(e) => setPrompt2(e.target.value)}
                            onKeyDown={handleSearch}
                            id="textfield2"
                            fullWidth
                            sx={{
                                mt: 2,
                                width: "90%",
                                display: isVisible2 ? "block" : "none",
                            }}
                        />
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSearch}
                            sx={{
                                mt: 4,
                                width: "100%",
                                padding: "12px",
                                fontSize: "16px",
                                borderRadius: "8px",
                            }}
                        >
                            Generate Story
                        </Button>
                    </Box>
                </Container>
            ) : (
                // Show StoryViewer when the user submits a search
                <StoryViewer
                    username={submittedUsername}
                    prompt={submittedPrompt}
                    prompt2={submittedPrompt2}
                    promptType={submittedType}
                />
            )}
        </>
    );
}
