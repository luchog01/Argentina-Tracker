import React from 'react'
import { useNavigate } from 'react-router-dom'
import "./Header.css"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBars } from '@fortawesome/free-solid-svg-icons'

const Header = ({ toggleMenu }) => {
    const navigate = useNavigate()

    return (
        <div className='header'>
            {/*location.pathname === '/graph' && <FontAwesomeIcon icon={faBars} className='bars' onClick={() => toggleMenu()}/>*/}
            <FontAwesomeIcon icon={faBars} className='bars' onClick={() => toggleMenu()}/>
            <div className='title-container' onClick={() => navigate('/graph/1')}>
                <img alt='' src={window.location.origin + '/logo.png'} className='icon'/>
                <h1 className='title'>FCI Tracker</h1>
                <div className='beta'>
                    <h5>(Beta)</h5>
                </div>
            </div>
        </div>
    )
}

export default Header