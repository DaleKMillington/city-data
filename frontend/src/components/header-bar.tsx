// Base Imports
import React from 'react';

// Interfaces
import { MenuItem } from '../interfaces/MenuItem.ts';

// Components
import HeaderMenu from "./header-menu.tsx";

// Props interface
interface HeaderBarProps {
  menuItems: MenuItem[];
}

const HeaderBar: React.FC<HeaderBarProps> = ({ menuItems}) => {
    return (
        <>
            <div className="header-bar">
                <h1 className="heading-primary">
                    <span className="heading-primary--main">Weather Data</span>
                </h1>
                <HeaderMenu menuItems={menuItems} />
            </div>
        </>
    )
}

export default HeaderBar;