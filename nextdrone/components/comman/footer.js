import React from 'react'
import Image from 'next/image'

function footer() {
    return (
        <>
            <footer>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12 col-xl-4">
                            <div className="footsec">
                                <div className="footlogocntSec">
                                    <a href="#" className="footlogo">
                                        {/* <Image style={{float:'left'}} height={78} width={130} className="img-fluid" src="/img/footlogo.svg" alt="img"/> */}
                                    </a>
                                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. </p>
                                </div>
                                <div className="joincommunity">
                                    <h3>Join the Community</h3>
                                    <ul>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/discordbutton.svg" alt="img" /></a></li>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/twitter.svg" alt="img" /></a></li>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/insta.svg" alt="img" /></a></li>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/reditbutton.svg" alt="img" /></a></li>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/youtube.svg" alt="img" /></a></li>
                                        <li><a href="#"><Image style={{ float: 'left' }} height={19} width={19} className="img-fluid" src="/img/emailbutton.svg" alt="img" /></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div className="col-lg-12 col-xl-8 d-none d-md-flex justify-content-between">
                            <div className="footlinks">
                                <h2>My account</h2>
                                <ul>
                                    <li><a href="#">Profile</a></li>
                                    <li><a href="#">Favorites</a></li>
                                    <li><a href="#">My collection</a></li>
                                    <li><a href="#">Settings</a></li>
                                </ul>
                            </div>

                            <div className="footlinks">
                                <h2>Discover</h2>
                                <ul>
                                    <li><a href="#">Art</a></li>
                                    <li><a href="#">Phorography</a></li>
                                    <li><a href="#">Domain Names</a></li>
                                    <li><a href="#">Memes</a></li>
                                    <li><a href="#">Virtual Worlds</a></li>
                                    <li><a href="#">Trading  Cards</a></li>
                                </ul>
                            </div>

                            <div className="footlinks">
                                <h2>Inform Center</h2>
                                <ul>
                                    <li><a href="aboutus.html">About Us</a></li>
                                    <li><a href="faq.html">FAQ</a></li>
                                    <li><a href="blogstyle1.html">Blog</a></li>
                                    <li><a href="contact.html">Contact</a></li>
                                    <li><a href="newsletter.html">Newsletter</a></li>
                                    <li><a href="#">Privacy Policy</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
            <div id="elevator_item"><a id="elevator" title="Back To Top"></a></div>
        </>
    )
}

export default footer