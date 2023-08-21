// Assets
import reactIcon from '../assets/react.svg';
import typescriptIcon from '../assets/typescript.svg';
import viteIcon from '../assets/vitejs.svg';
import djangoIcon from '../assets/django.svg';
import sassIcon from '../assets/sass.svg';
import pythonIcon from '../assets/python.svg';

const About = () => {
    return (
        <div className="about-container">

            <div className="about-card">
                <div className="about-card__title">
                    About
                </div>
                <div className="about-card__paragraph">
                    To view forecasted weather metrics for the next five days, please click on a city within the map.
                </div>
                <div className="about-card__paragraph">
                    Forecast metrics obtained via API from
                    <a className ="about-card__link" href="https://openweathermap.org/" target="_blank">
                        Open Weather Map
                    </a>.
                </div>
            </div>

            <a href="https://react.dev/" target="_blank">
                <img className="about-icon about-icon--one" src={ reactIcon } alt="React Icon" />
            </a>
            <a href="https://www.typescriptlang.org/" target="_blank">
                <img className="about-icon about-icon--two" src={ typescriptIcon } alt="Typescript Icon" />
            </a>
            <a href="https://vitejs.dev/" target="_blank">
                <img className="about-icon about-icon--three" src={ viteIcon } alt="Vitejs Icon" />
            </a>
            <a href="https://www.djangoproject.com/" target="_blank">
                <img className="about-icon about-icon--four" src={ djangoIcon } alt="Django Icon" />
            </a>
            <a href="https://sass-lang.com/" target="_blank">
                <img className="about-icon about-icon--five" src={ sassIcon } alt="Sass Icon" />
            </a>
            <a href="https://www.python.org/" target="_blank">
                <img className="about-icon about-icon--six" src={ pythonIcon } alt="Python Icon" />
            </a>
        </div>
    )
}

export default About;