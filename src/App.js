import React from 'react';
import illustration1 from './illustration1.svg';
import { Typography,  Slider, Paper } from '@material-ui/core';
import './App.css';

function App() {
 

  const marks = [
    { value: 0, label: "😔" },
    { value: 10, label: 1 },
    { value: 20, label: 2 },
    { value: 30, label: 3 },
    { value: 40, label: 4 },
    { value: 50, label: "😐" },
    { value: 60, label: 6 },
    { value: 70, label: 7 },
    { value: 80, label: 8 },
    { value: 90, label: 9 },
    { value: 100, label: "😊" }
  ];


  const scaler = (num) => {
    return num/10;
  }

  return (
    <div className="App" >
     <Typography style= {{paddingTop :60, paddingBottom:50}} variant="h1">
       How happy are you ?
     </Typography>
     <img src={illustration1} alt="svg" style= {{paddingTop :0, paddingBottom:50, width:450}}></img>
     <Slider
      style={{width: "60%" , marginTop:20, paddingBottom:50}}
      defaultValue={50}
      step={5}
      marks={marks}
      valueLabelDisplay="auto"
      scale={scaler}
/>
     <Typography style= {{paddingTop :20, paddingBottom: 40}} variant="subtitle1">
       See how you compare to the world 
     </Typography>

    <div className="paperbox">
     <Paper  style= {{width:160, height:160, margin:20 }}elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     <Paper  style= {{width:160, height:160, margin:20}} elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     <Paper  style= {{width:160, height:160, margin:20}} elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     <Paper  style= {{width:160, height:160, margin:20}} elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     <Paper  style= {{width:160, height:160, margin:20}} elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     <Paper  style= {{width:160, height:160, margin:20}} elevation={4} >
     <Typography style= {{padding :10, paddingTop:60}} variant="subtitle1">
       Sample Text 
     </Typography>
     </Paper>
     
     </div>
    </div>
  );
}

export default App;
