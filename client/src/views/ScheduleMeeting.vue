<template>
    <el-container>
        <el-row>

            <el-col class="desc" :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
                <img src="../assets/meeting.svg" alt="meeting-image" class="image"/>
                <div>
                    <h1 class="image-caption">Schedule Meetings With Ease!</h1>
                    <p class="image-sub-caption">Managing Meetings Now Much Easier</p>
                    <ul class="feature-list">
                        <li>Get instant meeting confirmation on email and mobile!</li>
                        <li>Schedule meeting from anywhere, anytime!</li>
                        <li>Schedule meeting using your mobile</li>
                        <li>Get check out email on your mailing address</li>
                        <li>Keep Track of All Visitors and Hosts</li>
                    </ul>
                </div>
            </el-col>

            <el-col class="form-div" :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
                <div v-if="!isMeetingConfirmed">
                    <el-col class="steps">
                        <el-steps align-center class="steps" :active="active">
                            <el-step title="Step 1" description="Visitor Details"></el-step>
                            <el-step title="Step 2" description="Host Details"></el-step>
                        </el-steps>
                    </el-col>


                    <el-form ref="form" :model="form" label-width="120px">
                        <div :class="{'show':isVisitor, 'hide':!isVisitor}">
                            <el-input
                                    name="visitor name"
                                    v-validate="'required|alpha_spaces'"
                                    prefix-icon="el-icon-user"
                                    class="form-input"
                                    placeholder="Visitor Name"
                                    v-model="form.visitor.name"/>
                            <p v-if="errors.has('visitor name')" class="registration-error-message">
                                {{errors.first("visitor name")}}</p>

                            <el-input
                                    name="visitor email"
                                    v-validate="'required|email'"
                                    prefix-icon="el-icon-message"
                                    class="form-input"
                                    placeholder="Visitor Email"
                                    v-model="form.visitor.email"/>
                            <p v-if="errors.has('visitor email')" class="registration-error-message">
                                {{errors.first("visitor email")}}</p>
                            <vue-phone-number-input
                                    @update="checkVisitorPhoneNo"
                                    v-validate="'required'"
                                    name="visitor phone number"
                                    v-model="visitorPhoneNo"
                                    class="form-input"/>
                            <p v-if="errors.has('visitor phone number')" class="registration-error-message">
                                {{errors.first("visitor phone number")}}</p>
                            <el-row>
                                <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
                                    <el-date-picker
                                            v-validate="'required'"
                                            name="visitor check-in"
                                            class="form-input"
                                            v-model="form.visitor.check_in"
                                            type="datetime"
                                            ref="check_in"
                                            placeholder="Visitor Check In"/>
                                    <p v-if="errors.has('visitor check-in')" class="registration-error-message">
                                        {{errors.first("visitor check-in")}}</p>
                                </el-col>
                                <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
                                    <el-date-picker
                                            v-validate="'required|after:check_in'"
                                            name="visitor check-out"
                                            class="form-input"
                                            v-model="form.visitor.check_out"
                                            type="datetime"
                                            placeholder="Visitor Check Out"/>
                                    <p v-if="errors.has('visitor check-out')" class="registration-error-message">
                                        {{errors.first("visitor check-out")}}</p>
                                </el-col>
                            </el-row>
                            <el-row>
                                <el-button
                                        @click="goToStepTwo"
                                        class="button"
                                        type="primary"
                                        round>Next <i class="el-icon-arrow-right"></i>
                                </el-button>
                            </el-row>
                        </div>
                        <div :class="{'show':!isVisitor, 'hide':isVisitor}">
                            <el-input
                                    name="host name"
                                    v-validate="'required|alpha_spaces'"
                                    prefix-icon="el-icon-user"
                                    class="form-input"
                                    placeholder="Host Name"
                                    v-model="form.name"/>
                            <p v-if="errors.has('host name')" class="registration-error-message">
                                {{errors.first("host name")}}</p>
                            <el-input
                                    name="host email"
                                    v-validate="'required|email'"
                                    prefix-icon="el-icon-message"
                                    class="form-input"
                                    placeholder="Host Email"
                                    v-model="form.email"/>
                            <p v-if="errors.has('host email')" class="registration-error-message">
                                {{errors.first("host email")}}</p>
                            <vue-phone-number-input
                                    @update="checkHostPhoneNo"
                                    name="host phone number"
                                    v-validate="'required'"
                                    v-model="hostPhoneNo"
                                    class="form-input"/>
                            <p v-if="errors.has('host phone number')" class="registration-error-message">
                                {{errors.first("host phone number")}}</p>
                            <el-button
                                    icon="el-icon-arrow-left"
                                    plain
                                    @click="goToStepOne"
                                    class="button"
                                    round>Back
                            </el-button>
                            <el-button
                                    @click="createMeeting"
                                    class="button"
                                    type="primary"
                                    round>Submit
                            </el-button>
                        </div>
                    </el-form>
                </div>

                <div v-else class="confirmation">
                    <h1 class="image-caption">All Set!</h1>
                    <p class="image-sub-caption">See you at our office</p>
                </div>
            </el-col>
        </el-row>
    </el-container>
</template>

<script>
    import meeting from "../api/meeting"

    export default {
        data: () => ({
            isVisitorPhoneNoValid: false,
            isHostPhoneNoValid: false,
            hostPhoneNo: '',
            visitorPhoneNo: '',
            active: 1,
            isVisitor: true,
            isMeetingConfirmed: false,
            form: {
                name: '',
                email: '',
                phone_no: '',
                visitor: {
                    name: '',
                    email: '',
                    phone_no: '',
                    check_in: '',
                    check_out: ''
                }
            }
        }),
        methods: {
            goToStepOne() {
                this.isVisitor = true
                this.active = 1
            },
            async goToStepTwo() {
                if (!this.isVisitorPhoneNoValid) {
                    this.$message({
                        showClose: true,
                        type: 'error',
                        message: "Please Check Visitor Phone Number"
                    })
                }
                if (
                    await this.$validator.validate('visitor name', this.form.visitor.name) &
                    await this.$validator.validate('visitor email', this.form.visitor.email) &
                    await this.$validator.validate('visitor phone number', this.form.visitor.phone_no) &
                    await this.$validator.validate('visitor check-in', this.form.visitor.check_in) &
                    await this.$validator.validate('visitor check-out', this.form.visitor.check_out) &
                    this.isVisitorPhoneNoValid) {
                    this.isVisitor = false
                    this.active = 2
                }
            },
            async createMeeting() {
                var global = this;
                if (!this.isHostPhoneNoValid) {
                    this.$message({
                        showClose: true,
                        type: 'error',
                        message: "Please Check Host Phone Number"
                    })
                }
                this.$validator.validate().then(valid => {
                    if (valid & this.isHostPhoneNoValid) {
                        this.form.visitor = [this.form.visitor]
                        console.log(this.form)
                        meeting.scheduleMeeting(global.form)
                            .then(() => this.isMeetingConfirmed = true)
                            .catch(error => {
                                this.$message({
                                    showClose: true,
                                    type: 'error',
                                    message: error.response.data
                                })
                            })
                    }
                });
            },
            checkVisitorPhoneNo(payload) {
                this.form.visitor.phone_no = payload.formattedNumber
                this.isVisitorPhoneNoValid = payload.isValid
            },
            checkHostPhoneNo(payload) {
                this.form.phone_no = payload.formattedNumber
                this.isHostPhoneNoValid = payload.isValid
            }
        }
    };
</script>

<style lang="css">
    .show {
        display: block;
    }

    .hide {
        display: none;
    }

    .image {
        width: 80%;
        margin: 1rem auto;
    }

    .steps {
        margin: 0 0 1rem 0;
    }

    .image-sub-caption {
        color: rgb(120, 120, 120);
        font-weight: 600;
        padding-bottom: 1rem;
    }

    .feature-list {
        margin: 1rem;
        list-style: none;
    }

    .feature-list > li {
        font-weight: 400;
        color: rgb(120, 120, 120);
        padding: 0.4rem 0;
    }

    .desc, .confirmation{
        text-align: center;
    }

    .desc {
        background-color: #e6f1ff;
    }

    .registration-error-message {
        color: #f56c6c;
        font-size: 13px;
        line-height: 1;
        padding-top: 4px;
        position: relative;
        margin: -1rem 0 1rem 0;
        top: 100%;
        left: 0;
    }

    .form-div {
        padding: 3rem;
    }

    .form-input {
        border: none !important;
        margin: 1rem 0;
    }

    .button {
        margin: 2rem 0;
    }
</style>
