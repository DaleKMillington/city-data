// Base Imports
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Interfaces
import { MenuItem } from './interfaces/MenuItem.ts';

// Components
import HeaderBar from './components/HeaderBar.tsx';

// Pages
import Map from './pages/Map.tsx';
import About from './pages/About.tsx';

const App = () => {

    // Define the different menu items
    const menuItems: MenuItem[] = [
        { text: 'Map', path: '/' },
        { text: 'About', path: '/about' },
    ];

    return (
        <Router>
            <HeaderBar menuItems={ menuItems }/>
            <Routes>
                <Route path="/" Component={ Map } />
                <Route path="/about" Component={ About } />
            </Routes>
        </Router>
    )
}

export default App
