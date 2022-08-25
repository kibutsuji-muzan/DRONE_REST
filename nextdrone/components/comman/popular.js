import React from 'react'
import Image from 'next/image'
import Item from './item'
import Slider from 'react-slick'

function PopularCollection() {

    const settings = {
        dots: false,
        arrows: true,
        infinite: false,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    arrows: false,
                    dots: true
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    dots: true
                }
            }

        ]
    }

    return (
        <div className="popularCollection mt-4 pt-4 mt-md-5 pt-md-5 mt-lg-5 pt-lg-5">
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h2 className="headingWh mb-4">Popular collections</h2>
                        <div className="tab-sec">
                            <nav>
                                <div className="nav nav-tabs" id="nav-tab" role="tablist">
                                    <button className="nav-link d-none d-sm-none d-md-block active" data-bs-toggle="tab" data-bs-target="#TabOne">All categories</button>
                                    <button className="nav-link d-none d-sm-none d-md-block" data-bs-toggle="tab" data-bs-target="#TabTwo">Digital</button>
                                    <button className="nav-link d-none d-sm-none d-md-block" data-bs-toggle="tab" data-bs-target="#TabThree">Photography</button>
                                    <button className="nav-link d-none d-sm-none d-md-block" data-bs-toggle="tab" data-bs-target="#TabFour">Memes</button>
                                    <div className="more-tab">
                                        <a href="javascript:void(0)" className="textbluecolor categorytab">Choose category <Image width={14} height={14} src="/img/bluedown.png" alt="arrow-down" /></a>
                                        <div className="more-box nav nav-tabs" id="more_tab" role="tablist">
                                            <button className="nav-link active" data-bs-toggle="tab" data-bs-target="#TabOne">All categories</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#TabTwo">Digital</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#TabThree">Photography</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#TabFour">Memes</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg1">All categories</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg2">Memes</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg3">Photography</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg4">Digital</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg5">News</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg6">Music</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg7">Domain names</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg8">Virtual worlds</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg9">Trading cards</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg10">Sports</button>
                                            <button className="nav-link" data-bs-toggle="tab" data-bs-target="#tabcatg11">Utility</button>
                                        </div>
                                    </div>
                                </div>
                            </nav>

                            <div className="tab-content" id="nav-tabContent">
                                {/* <div className="tab-pane fade show active" id="TabOne">
                                    
                                    <div className="popular slider">

                                        <Item type='popular'/>
                                        
                                        </div>
                                    </div> */}
                                <Slider {...settings}>
                                    <Item type='popular' />
                                    <Item type='popular' />
                                    <Item type='popular' />
                                    <Item type='popular' />
                                    <Item type='popular' />
                                    <Item type='popular' />
                                </Slider>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default PopularCollection