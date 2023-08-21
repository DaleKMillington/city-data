// Base Imports
import { useState } from 'react';
import { Link } from 'react-router-dom';

// Interfaces
import { MenuItem } from '../interfaces/MenuItem.ts';
interface HeaderBarProps {
  menuItems: MenuItem[];
}

// Represents the menu button and contents.
const HeaderMenu = ({ menuItems }: HeaderBarProps) => {

    // Hooks
    const [isOpen, setIsOpen] = useState(false);
    const toggleDropdown = () => setIsOpen(!isOpen);

    return (
        <>
            <div className="header-menu">
                <button className="header-menu__button" onClick={ toggleDropdown }>MENU</button>
            </div>
            { isOpen && (
                    <ul className="header-menu-list">
                        {
                            menuItems.map((item: MenuItem, index: number) => (
                                <li key={ index } className="header-menu-list__item">
                                    <Link to={ item.path } className="header-menu-list__link" onClick={ toggleDropdown }>
                                        { item.text }
                                    </Link>
                                </li>
                            ))
                        }
                    </ul>
                )
            }
        </>
    )
}

export default HeaderMenu;