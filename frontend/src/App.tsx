// Interfaces
import { MenuItem } from './interfaces/MenuItem.ts';

// Components
import HeaderBar from './components/header-bar.tsx';

const App = () => {

    // Define the different menu items
    const menuItems: MenuItem[] = [
        { text: 'Main', link: '#' },
        { text: 'About', link: '#' },
    ];

    return (
        <HeaderBar menuItems={ menuItems }/>
    )
}

export default App
