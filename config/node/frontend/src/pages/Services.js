import React from 'react';
import {Button} from "@mui/material";
import {Link} from 'react-router-dom';


function Services() {
    return (
        <div className='services'>
            <div className='services__title'>Services</div>
            <Button
                className="map__button"
                variant="contained"
                size="large"
                component={Link}
                to='/map'
            >
                Do map
            </Button>
            <Button
                className="list__button"
                variant="contained"
                size="large"
                component={Link}
                to='/list'
            >
                Do list
            </Button>


        </div>
    );
}

export default Services;