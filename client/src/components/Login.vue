<!-- Login page for webapp --> 

<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>UC Basic Needs</h1>
          <FormulateForm
            class="login-form"
            v-model="formValues"
          >
            <h2 class="form-title">Register</h2>
            <p>
            Welcome to the UC Basic Needs landing page! It looks like this is your first time here. Please register by filling the fields below. 
            </p>
            <FormulateInput
              type="email"
              label="UC email"
              name="email"
              validation="bail|required|email|ends_with:ucsc.edu,berkeley.edu,ucla.edu,ucsd.edu,ucsb.edu,ucdavis.edu,uci.edu,ucr.edu,ucmerced.edu,
              "
            />
            <br>
            <FormulateInput
              type="text"
              label="Student ID"
              name="Student ID"
              validation="bail|required|number"
            />
            <br>
            <FormulateInput
              type="text"
              label="Preferred Name"
              name="Name"
              validation="bail|required"
            />
            <br>
            <FormulateInput
              type="submit"
              name="Submit"
            />
        </FormulateForm>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      formValues: {}
    }
  }
}
</script>

<style scoped>
.login-form {
  padding: 2em;
  border: 1px solid #a8a8a8;
  border-radius: .5em;
  max-width: 500px;
  box-sizing: border-box;
}
.form-title {
  margin-top: 0;
}
.login-form::v-deep .formulate-input .formulate-input-element {
  max-width: none;
}
@media (min-width: 420px) {
  .double-wide {
    display: flex;
  }
  .double-wide .formulate-input {
    flex-grow: 1;
    width: calc(50% - .5em);
  }
  .double-wide .formulate-input:first-child {
    margin-right: .5em;
  }
  .double-wide .formulate-input:last-child {
    margin-left: .5em;
  }
}
</style>