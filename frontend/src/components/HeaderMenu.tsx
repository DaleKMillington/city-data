// Base Imports
import React from 'react';
import { Link, Outlet } from 'react-router-dom';

// Hooks
import { useState } from 'react';

// Interfaces
import { MenuItem } from '../interfaces/MenuItem.ts';

// Props interface
interface HeaderBarProps {
  menuItems: MenuItem[];
}

const HeaderMenu: React.FC<HeaderBarProps> = ({ menuItems }) => {
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
            <Outlet/>
        </>
    )
}

export default HeaderMenu;