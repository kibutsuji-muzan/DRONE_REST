import React from 'react'
import Slider from 'react-slick'
import Item from '/components/comman/item'

function LastAdded() {
    const settings = {
        dots: false,
        arrows: true,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
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
        <div className="LastAddedItems pt-3">
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h2 className="headingWh mb-3 mb-sm-3 mb-md-4 mb-xl-5">Last Added Items</h2>
                        <Slider {...settings} className="slider">

                            <Item type='lastadded'/>

                            <Item type='lastadded'/>

                            <Item type='lastadded'/>

                            <Item type='lastadded'/>

                            <Item type='lastadded'/>

                            <Item type='lastadded'/>

                        </Slider>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default LastAdded
