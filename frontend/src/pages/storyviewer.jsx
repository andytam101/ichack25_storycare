import { useState, useEffect } from "react";
import { Box, Typography, Container, CircularProgress } from "@mui/material";
import { motion } from "framer-motion";

export default function StoryViewer({ prompt }) {
    const [storyData, setStoryData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simulated API call - replace with actual fetch from backend
        const fetchStory = async () => {
            setLoading(true);
            try {
                // Replace with your backend API
                const response = await fetch(`https://your-backend.com/generate-story?prompt=${prompt}`);
                const data = await response.json();
                setStoryData(data);
            } catch (error) {
                console.error("Error fetching story:", error);
            }
            setLoading(false);
        };

        fetchStory();
    }, [prompt]);

    if (loading) return <CircularProgress sx={{ display: "block", margin: "auto", mt: 5 }} />;

    return (
        <Container maxWidth="md">
            {storyData?.map((item, index) => (
                <Box key={index} sx={{ minHeight: "100vh", position: "relative" }}>
                    {/* Fullscreen Image */}
                    <Box
                        component="img"
                        src={item.imageUrl}
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
                            {item.chapterTitle}
                        </Typography>
                        <Typography variant="body1" color="textSecondary">
                            {item.chapterText}
                        </Typography>
                    </motion.div>
                </Box>
            ))}
        </Container>
    );
}
