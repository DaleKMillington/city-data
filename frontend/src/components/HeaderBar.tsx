// Components
import HeaderMenu from "./HeaderMenu.tsx";

// Interfaces
import { MenuItem } from '../interfaces/MenuItem.ts';
interface HeaderBarProps {
    menuItems: MenuItem[];
}

// Represents the top header bar.
const HeaderBar = ({ menuItems}: HeaderBarProps) => {
    return (
        <div className="header-bar">
            <h1 className="heading-primary">
                <span className="heading-primary--main">City Data</span>
            </h1>
            <HeaderMenu menuItems={menuItems} />
        </div>
    )
}

export default HeaderBar;