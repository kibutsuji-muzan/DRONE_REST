import Image from 'next/image'
import React from 'react'

function OwnerSection() {
    return (
        <div className="authoreprofile authoSm mt-0 mt-md-5 pt-0 pt-md-2">
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <div className="authoreproimg">
                            <div className="authoreproimgBox">
                                <div className='d-none d-md-block'>
                                <Image className="img-fluid" height={300} width={1180} src="/drone.jpg" alt="img" />
                                </div>

                                <div className='d-block d-md-none'>
                                <Image className="img-fluid" height={250} width={540} src="/drone.jpg" alt="img" />
                                </div>
                            </div>
                            <div className="authoreproicon"><img className="img-fluid" height={130} width={130} style={{ float: 'left' }} src="/attachment_127148423.png" alt="img" /></div>
                        </div>
                        <div className="auProfileDetail">
                            <div className="joincommunity auSocial">

                                <ul>
                                    <li><a href="#"><Image className="img-fluid" height={18} width={18} style={{ float: 'left' }} src="/img/activityicon.svg" alt="img" /></a></li>
                                    <li><a href="#"><Image className="img-fluid" height={18} width={18} style={{ float: 'left' }} src="/img/discordbutton.svg" alt="img" /></a></li>
                                    <li><a href="#"><Image className="img-fluid" height={18} width={18} style={{ float: 'left' }} src="/img/insta.svg" alt="img" /></a></li>
                                    <li><a href="#"><Image className="img-fluid" height={18} width={18} style={{ float: 'left' }} src="/img/twitter.svg" alt="img" /></a></li>
                                </ul>

                            </div>
                            <div className="prCnt">
                                <h2 className="textwhitecolor">Ringers by Dmitri Cherniak</h2>
                                <h3 className="textgraycolor mt-3 mb-4"><span className="textbluecolor">Last updated:</span> October 21st, 2021 at
                                    3 AM</h3>
                                <p className="textgraycolor">There are many variations of passages of Lorem Ipsum available, but<br /> the
                                    majority have suffered alteration in some form, by injected</p>
                            </div>

                        </div>
                        <div className="showResultTop">
                            <ul>
                                <li>
                                    <span className="textgraycolor">Items</span>
                                    <strong className="textwhitecolor"></strong>
                                </li>

                                <li>
                                    <span className="textgraycolor">Owners</span>
                                    <strong className="textwhitecolor"></strong>
                                </li>

                                <li>
                                    <span className="textgraycolor">Floor Price</span>
                                    <strong className="textwhitecolor"><Image className="img-fluid" height={13} width={9} style={{ float: 'left',filter:"invert(1)"}} src="/img/priceicon.svg" alt="img" /></strong>
                                </li>

                                {/* <li>
                                    <span className="textgraycolor">Volume Traded</span>
                                    <strong className="textwhitecolor"><Image className="img-fluid" height={13} width={9} style={{ float: 'left',filter:"invert(1)" }} src="/img/priceicon.svg" alt="img" /></strong>
                                </li> */}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default OwnerSection