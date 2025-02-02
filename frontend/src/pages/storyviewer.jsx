import { useState, useEffect } from "react";
import { Box, Typography, Container, CircularProgress } from "@mui/material";
import { motion } from "framer-motion";

export default function StoryViewer({ prompt, prompt2, promptType }) {
    const [storyData, setStoryData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchStory = async () => {
            setLoading(true);
            try {
                const response = await fetch("http://127.0.0.1:5000/generate-story", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                    body: JSON.stringify({ prompt, prompt2, promptType }), // Send prompt in body
                });

                if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

                const data = await response.json();
                setStoryData(data);
            } catch (error) {
                console.error("Error fetching story:", error);
            }
            setLoading(false);
        };

        fetchStory();
    }, [prompt, prompt2, promptType]);

    if (loading) return <CircularProgress sx={{ display: "block", margin: "auto", mt: 5 }} />;

    return (
        <Container maxWidth="md">
            {storyData?.captions?.map((caption, index) => (
                <Box key={index} sx={{ minHeight: "100vh", position: "relative" }}>
                    {/* Fullscreen Image */}
                    <Box
                        component="img"
                        src={storyData.images[index]} // Fetch image from response
                        alt={`Story part ${index + 1}`}
                        sx={{
                            width: "100%",
                            height: "100vh",
                            objectFit: "cover",
                            display: "block",
                        }}
                    />

                    {/* Story Chapter - Revealed on Scroll */}
                    <motion.div
                        initial={{ opacity: 0, y: 50 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                        viewport={{ once: true }}
                        style={{
                            padding: "2rem",
                            backgroundColor: "white",
                            textAlign: "center",
                        }}
                    >
                        <Typography variant="h4" gutterBottom>
                            Chapter {index + 1}
                        </Typography>
                        <Typography variant="body1" color="textSecondary">
                            {caption}
                        </Typography>
                    </motion.div>
                </Box>
            ))}
        </Container>
    );
}

