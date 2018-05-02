import React, { Component } from 'react';
import Image from 'react-simple-image'
//import Tools from '../BrewTool_content/Tools'

class NavBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }

    render () {
        return (
            <div>
              <div className='col-lg-6 col-xs-6'>
                <div className='col-lg-8 col-xs-8 col-lg-offset-2 col-xs-offset-2'>
                  <Image
                      className='col-lg-6 col-xs-6'
                      alt='no image'
                      src='/static/images/LogoTop.jpg'
                      srcSet={{
                        '360w': '/static/images/LogoTop.jpg',
                      }}
                  />
                  <div className='col-lg-6 col-xs-6 Company'>
                    <p> WEIN-TM </p>
                  </div>
                </div>
              </div>

              <div className='col-lg-6 col-xs-6 Buttons'>
                <p>home</p>
                <p>details</p>
                <p>portfolio</p>
                <p>timeline</p>
                <p>featured</p>
                <p>dots</p>
              </div>

            </div>
        )
    }
}

class MainImage extends Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }

  render() {
    return (
        <div>
          <div className='col-lg-12 col-xs-12'>
            <Image
                alt='no image'
                src='/static/images/MainImage.jpg'
                srcSet={{
                  '360w': '/static/images/MainImage.jpg',
                }}
            />

            <div className='WhoIs'>
              <h2>Tattoo Machines</h2>
              <h5>Great CraftsMan</h5>
            </div>
          </div>

        </div>
    )
  }

}


class BasicInfo extends Component {

  render() {
    return (
        <div>
          <div className='col-lg-3 col-xs-3 InfoBlock'>
            <div className='col-lg-1 col-xs-1'>
              <Image/>
            </div>
            <div className='col-lg-10 col-xs-10'>
              <h5> Creative </h5>
              <p> Description </p>
            </div>
          </div>

          <div className='col-lg-3 col-xs-3 InfoBlock'>
            <h5> Self-Motivated </h5>
            <p> Description </p>
          </div>

          <div className='col-lg-3 col-xs-3 InfoBlock'>
            <h5> Punctial </h5>
            <p> Description </p>
          </div>

          <div className='col-lg-3 col-xs-3 InfoBlock'>
            <h5> Multitask </h5>
            <p> Description </p>
          </div>
        </div>
    )
  }
}


class LandingContent extends Component {
    constructor(props) {
        super(props);
        this.state = {
        };
    }


    render () {
        return (
            <div className="LandingNew">

              <div className='NavBar'>
                <NavBar/>
              </div>

              <div className='MainImage'>
                <MainImage/>
              </div>

              <div className='BasicInfo'>
                <BasicInfo/>
              </div>

                <div className='Stats'>

                </div>

                <div className='Goods'>

                </div>

                <div className='Diagram'>

                </div>

                <div className='Timeline'>

                </div>

                <div className='Photos'>

                </div>

                <div className='Reviews'>

                </div>

                <div className='ContactForm'>

                </div>

                <div className='Footer'>

                </div>
            </div>
        );
    }
}

export default LandingContent;