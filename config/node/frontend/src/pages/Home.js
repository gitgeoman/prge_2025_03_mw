import React from 'react';
import {Typography, Button} from "@mui/material";
import {Link} from "react-router-dom";

import './Home.css';

function Home() {

    return (<div className="home">
        <h1 className="home__title"> GEOPORTAL</h1>

        <Typography className="home__subtitle">
            Geoportal tematyczny poświęcony danym przestrzennym
        </Typography>

        <Button
            className="home__button"
            variant="contained"
            size="large"
            component={Link}
            to='services'
        >
            START
        </Button>

    </div>);
}


export default Home;