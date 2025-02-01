import { Box, Typography, TextField, Container } from "@mui/material";

export default function Home() {
    return (
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
                    placeholder="Search..."
                    fullWidth
                    sx={{ mt: 2 }}
                />
            </Box>
        </Container>
    );
}
