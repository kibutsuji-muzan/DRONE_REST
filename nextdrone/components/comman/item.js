import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
// import { useContext } from 'react'
// import { DataContext } from '/pages/products'

function Item(props) {

    const condition = props.type

    if (condition == 'lastadded') {
        return (

            // <div className="col-md-6 col-xl-3 mb-4">
                <Link href="item/">
                    <a>
                        <div className="aboutitem">
                            <div className="aboutitemImg"><Image layout='responsive' style={{ float: 'left' }} className="img-fluid" width={265} height={240} src="/download.jpeg" alt="img" /></div>
                            <div className="bgdarkbluecolor aboutitemcnt">
                                <div className="itemtitlecode">
                                    <h2 className="textgraycolor">RTFKT Creators</h2>
                                    <h3 className="textwhitecolor">Lorem Ipsum is simply</h3>
                                </div>
                                <div className="itemtitlePrice">
                                    <h2 className="textgraycolor">Price</h2>
                                    <h3 className="textwhitecolor"><Image width={12} height={17} style={{filter:"invert(1)"}} src="/img/priceicon.svg" /> <strong>6,000</strong></h3>
                                    <h4 className="textgraycolor"><span><Image width={15} height={13} src="/img/hearticon.svg" /></span> 56</h4>
                                </div>
                            </div>
                        </div>
                    </a>
                </Link>
            //</div> 

        )
    } else if (props.type == 'popular') {

        return (
            <Link href="item/">
                <a>
                    <div className="creators">
                        <div className="creatorImg"><Image width={375} height={170} className="img-fluid" src="/drone.jpg" alt="img" /></div>
                        <div className="creatorIcon">
                            <Image width={65} height={65} className="img-fluid" src="/attachment_127148423.png" alt="imig" />
                            <div className="creatorcheck"><Image width={19} height={19} src="/img/checkicon.svg" alt="img" /></div>
                        </div>
                        <div className="creatorsText text-center">
                            <h2 className="textwhitecolor">RTFKT Creators</h2>
                            <h3 className="textbluecolor">by RTFKT</h3>
                            <p className="textgraycolor">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                        </div>
                    </div>
                </a>
            </Link>
        )
    }

}

export default Item