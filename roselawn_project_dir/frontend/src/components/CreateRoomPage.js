import React, { Component } from "react";
import { Grid, Button, Typography, TextField, FormLabel } from "@mui/material";
import { Radio, RadioGroup } from "@mui/material";
import { FormControl, FormControlLabel, FormHelperText } from "@mui/material";
import { Link } from "react-router-dom"

export default class CreateRoomPage extends Component {
    default_votes = 2;
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h4' variant='h4'>
                        Create a ROOOOOm 1248
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component='fieldset'>
                        <FormHelperText>
                            <div align='center'> Guest can Skip maybe</div>
                        </FormHelperText>
                        <RadioGroup row defaultValue="True">
                            <FormControlLabel
                                value='True'
                                control={<Radio color="primary"/>}
                                label="Play/Pause"
                                labelPlacement="bottom" 
                            />
                            <FormControlLabel
                                value='False'
                                control={<Radio color="secondary"/>}
                                label="No Control"
                                labelPlacement="bottom" 
                            />
                        </RadioGroup>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component='fieldset'>
                        <TextField
                            required={true} 
                            type="number" 
                            defaultValue={this.default_votes}
                            inputProps={{
                                min: 1,
                                style: {textAlign:'center'}
                                }}
                        />
                        <FormHelperText>
                            <div align='center'>
                                Votes required to skip song
                            </div>
                        </FormHelperText>
                    </FormControl>
                </Grid>
                <Grid item xs={12} align='center'>
                    <Button color="secondary" variant='contained'>
                        Create a Room
                    </Button>
                </Grid>
                <Grid item xs={12} align='center'>
                    <Button color="primary" variant='contained' to='/' component={Link}>
                        Back
                    </Button>
                </Grid>
            </Grid>
        );
    }
}