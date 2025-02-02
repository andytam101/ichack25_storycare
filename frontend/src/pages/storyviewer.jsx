import { useState, useEffect } from "react";
import { Box, Typography, Container, CircularProgress, IconButton } from "@mui/material";
import { ArrowBack, ArrowForward } from "@mui/icons-material";
import { motion } from "framer-motion";

export default function StoryViewer({ username, prompt, prompt2, promptType }) {
    const [storyData, setStoryData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [index, setIndex] = useState(0);
    
    const handleLeftArrowClick = () => {
        setIndex(prev => (prev > 0 ? prev - 1 : prev));
    };

    const handleRightArrowClick = () => {
        setIndex(prev => (prev < storyData.images.length - 1 ? prev + 1 : prev));
    };

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
                    body: JSON.stringify({ username, prompt, prompt2, promptType }),
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
    }, [username, prompt, prompt2, promptType]);

    if (loading) return <CircularProgress sx={{ display: "block", margin: "auto", mt: 5 }} />;

    return (
        <>
            <IconButton 
                href="/" 
                sx={{ 
                    position: "absolute", 
                    top: 40, 
                    left: 40, 
                    backgroundColor: "rgba(0, 0, 0, 0.5)", 
                    color: "white", 
                    borderRadius: "12px",
                    width: "120px",
                    paddingTop: "9px",
                    paddingBottom: "9px",
                    "&:hover": { backgroundColor: "rgba(0, 0, 0, 0.7)" } 
                }}
            >
                Home
            </IconButton>
        
            <Container
                maxWidth="md"
                sx={{ 
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    height: "100vh",
                    position: "relative"
                }}
            >
                {/* Left Arrow */}
                <IconButton 
                    onClick={handleLeftArrowClick} 
                    sx={{ 
                        position: "absolute",
                        left: 10, 
                        top: "50%", 
                        transform: "translate(-150%, -100%)", 
                        backgroundColor: "rgba(0, 0, 0, 0.5)", 
                        color: "white", 
                        "&:hover": { backgroundColor: "rgba(0, 0, 0, 0.7)" },
                    }}
                    style = {{ display: index > 0 ? "block" : "none" }}
                    id="left-arrow"
                >
                    <ArrowBack fontSize="large" />
                </IconButton>

                {/* Main Content */}
                <Box sx={{ textAlign: "center" }}>
                    {/* Image */}
                    <Box
                        component="img"
                        src={storyData.images[index]} 
                        alt={`Story part ${index + 1}`}
                        sx={{
                            width: "100%",
                            maxHeight: "70vh",
                            objectFit: "cover",
                            borderRadius: "10px",
                            boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)"
                        }}
                    />

                    {/* Story Chapter */}
                    <motion.div
                        initial={{ opacity: 0, y: 50 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                        style={{
                            padding: "1.5rem",
                            backgroundColor: "white",
                            borderRadius: "10px",
                            boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)",
                            marginTop: "20px"
                        }}
                    >
                        <Typography variant="h4" gutterBottom>
                            Chapter {index + 1}
                        </Typography>
                        <Typography variant="body1" color="textSecondary">
                            {storyData.captions[index]}
                        </Typography>
                    </motion.div>
                </Box>

                {/* Right Arrow */}
                <IconButton 
                    onClick={handleRightArrowClick} 
                    sx={{ 
                        position: "absolute", 
                        right: 10, 
                        top: "50%", 
                        transform: "translate(150%, -100%)", 
                        backgroundColor: "rgba(0, 0, 0, 0.5)", 
                        color: "white", 
                        "&:hover": { backgroundColor: "rgba(0, 0, 0, 0.7)" } 
                        
                    }}
                    id="right-arrow"
                    style = {{ display: index < storyData.images.length - 1? "block" : "none" }}
                >
                    <ArrowForward fontSize="large" />
                </IconButton>
            </Container>
        </>
    );
}
