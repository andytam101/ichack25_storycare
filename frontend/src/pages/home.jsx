import { useState } from "react";
import { Box, Typography, TextField, Container, Button } from "@mui/material";
import StoryViewer from "./storyviewer"; // Import the story viewer

export default function Home() {
    const [prompt, setPrompt] = useState("");
    const [submittedPrompt, setSubmittedPrompt] = useState(null);

    const handleSearch = (event) => {
        if (event.key === "Enter" || event.type === "click") {
            setSubmittedPrompt(prompt); // Send prompt to StoryViewer
        }
    };

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
                            A personalized journey through healing and hope.
                        </Typography>
                        <TextField
                            variant="outlined"
                            placeholder="Enter a disease..."
                            fullWidth
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            onKeyDown={handleSearch}
                            sx={{ mt: 2 }}
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
                <StoryViewer prompt={submittedPrompt} />
            )}
        </>
    );
}

