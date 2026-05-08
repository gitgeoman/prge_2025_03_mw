import './App.css';

import {RouterProvider} from 'react-router-dom';
import routes from "./routes/Router";

function App() {

    return (
        <div className="App">
            <RouterProvider router={routes}/>
        </div>
    );
}

export default App;
