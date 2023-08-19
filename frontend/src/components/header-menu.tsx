// Base Imports
import React from 'react';

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
                                    <a href={ item.link } className="header-menu-list__link">{ item.text }</a>
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